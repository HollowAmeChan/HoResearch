"""Launch a local, isolated Blender MMD reference-rendering job."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys


def discover_blender():
    candidates = [shutil.which("blender")]
    if os.name == "nt":
        candidates += [str(p) for p in sorted(Path("D:/Blender").glob("blender-4.5*/blender.exe"), reverse=True)]
        candidates += [str(p) for p in Path("C:/Program Files/Blender Foundation").glob("Blender */blender.exe")]
    return next((p for p in candidates if p and Path(p).is_file()), None)


def discover_addons():
    base = Path(os.environ.get("APPDATA", Path.home())) / "Blender Foundation/Blender"
    candidates = sorted(base.glob("4.5/scripts/addons/mmd_tools/__init__.py"), reverse=True)
    candidates += sorted(base.glob("*/scripts/addons/mmd_tools/__init__.py"), reverse=True)
    return str(candidates[0].parents[1]) if candidates else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pmx", required=True, type=Path)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--blender")
    parser.add_argument("--mmd-addons")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--model-id")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--preview", action="store_true")
    modes.add_argument("--all", action="store_true")
    parser.add_argument("--head-bone")
    parser.add_argument("--ortho-scale", type=float)
    parser.add_argument("--target-offset", type=float, nargs=3, default=[0, 0, 0], metavar=("RIGHT", "FRONT", "UP"))
    parser.add_argument("--samples", type=int, default=128)
    parser.add_argument("--size", type=int, default=512)
    args = parser.parse_args()
    repo = args.repo.resolve()
    source = args.pmx.resolve()
    if not source.is_file() or source.suffix.lower() not in {".pmx", ".pmd"}:
        parser.error("请提供实际存在的 PMX / PMD 文件。")
    if not (repo / ".git").exists():
        parser.error("--repo 必须指向已配置 IGNORE/ 的研究仓库。")
    check = subprocess.run(["git", "-C", str(repo), "check-ignore", "-q", "--", "IGNORE/runs/check"], capture_output=True)
    if check.returncode != 0:
        parser.error("IGNORE/ 未被 Git 忽略；请先修复仓库 .gitignore。")
    if source.is_relative_to(repo):
        if not source.is_relative_to(repo / "IGNORE"):
            parser.error("仓库内的原始模型包及贴图应一起放入 IGNORE/models/，不能只依赖 *.pmx 忽略规则。")
        check = subprocess.run(["git", "-C", str(repo), "check-ignore", "-q", "--", source.relative_to(repo).as_posix()], capture_output=True)
        if check.returncode != 0:
            parser.error("仓库内的原始模型必须先放入 Git 忽略目录。")
        tracked = subprocess.run(["git", "-C", str(repo), "ls-files", "--error-unmatch", "--", source.relative_to(repo).as_posix()], capture_output=True)
        if tracked.returncode == 0:
            parser.error("原始模型已被 Git 跟踪；先保留本地文件并将其移出索引。")
    config_path = repo / "IGNORE/config/mmd-expression-reference.local.json"
    config = json.loads(config_path.read_text(encoding="utf-8-sig")) if config_path.exists() else {}
    blender = args.blender or config.get("blender") or discover_blender()
    addons = args.mmd_addons or config.get("mmd_addons") or discover_addons()
    if not blender or not Path(blender).is_file():
        parser.error("找不到 Blender；请设置 --blender 或本机配置。")
    if not addons or not (Path(addons) / "mmd_tools/__init__.py").is_file():
        parser.error("找不到 mmd_tools；--mmd-addons 应指向包含该插件的 addons 目录。")
    if args.samples < 1 or args.size < 32 or (args.ortho_scale is not None and args.ortho_scale <= 0):
        parser.error("尺寸、采样和取景尺度必须为正数。")
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    slug = re.sub(r'[<>:"/\\|?*\s]+', "_", source.stem).strip(" ._")[:48] or "model"
    model_id = args.model_id or f"{slug}_{source_hash[:8]}"
    if model_id in {".", ".."} or re.search(r'[<>:"/\\|?*]', model_id):
        parser.error("--model-id 必须为单个合法目录名。")
    output = args.output or Path("mmd表情调查/模型参考") / model_id
    output = (output if output.is_absolute() else repo / output).resolve()
    private = repo / "IGNORE/runs" / model_id
    private.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)
    job = {
        "source": str(source), "source_sha256": source_hash, "repo": str(repo),
        "output": str(output), "private": str(private), "addons": str(Path(addons).resolve()),
        "preview": args.preview, "head_bone": args.head_bone,
        "ortho_scale": args.ortho_scale, "target_offset": args.target_offset,
        "samples": args.samples, "size": args.size, "material_profile": "eevee-reference-toon-v1",
    }
    job_path = private / "job.json"
    job_path.write_text(json.dumps(job, ensure_ascii=False, indent=2), encoding="utf-8")
    worker = Path(__file__).with_name("blender_pipeline.py")
    command = [str(blender), "-b", "--factory-startup", "--disable-autoexec", "--python-exit-code", "1", "--python", str(worker), "--", str(job_path)]
    log_path = private / ("preview.log" if args.preview else "render.log")
    print(f"Blender: {blender}\nOutput: {output}\nLog: {log_path}", flush=True)
    with log_path.open("w", encoding="utf-8") as stream:
        result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT)
    if result.returncode:
        print(log_path.read_text(encoding="utf-8", errors="replace")[-12000:], file=sys.stderr)
        raise SystemExit(result.returncode)
    subprocess.run([sys.executable, str(Path(__file__).with_name("report.py")), str(output), "--statistics", str(repo / "mmd表情调查/附录/mmd_morph_names_all.txt")], check=True)
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    if manifest["validation_errors"] or (not args.preview and not manifest["complete"]):
        raise RuntimeError("渲染结果不完整，详见 manifest.json。")
    print(json.dumps({"report": str(output / "参考表.md"), "complete": manifest["complete"], "source_morphs": manifest["source_morph_count"], "rendered": len(manifest["expressions"])}, ensure_ascii=False))


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    main()
