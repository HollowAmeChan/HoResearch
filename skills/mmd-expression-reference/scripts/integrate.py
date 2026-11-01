"""Register a validated full-model render in the shared research reference table."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

from PIL import Image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--study", type=Path, default=Path(__file__).resolve().parents[3] / "mmd表情调查")
    parser.add_argument("--label", required=True)
    parser.add_argument("--key", required=True, help="例如 05_TDA_MTrace；数字前缀决定主表列顺序")
    parser.add_argument("--credit", default="")
    args = parser.parse_args()
    if not re.fullmatch(r"\d+_[A-Za-z0-9_-]+", args.key):
        parser.error("--key 必须包含数字前缀和安全的英文标识。")
    path = args.manifest.resolve()
    source = path.parent
    study = args.study.resolve()
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if not manifest["complete"] or manifest["validation_errors"]:
        parser.error("只可加入已经完整渲染且核验通过的模型。")
    if len(manifest["expressions"]) != manifest["source_morph_count"]:
        parser.error("源 morph 数量与已渲染数量不符。")
    if not manifest.get("armature") or not manifest.get("meshes"):
        parser.error("渲染清单缺少真实骨架/网格信息，请使用当前管线重新生成。")
    target = study / (args.key + "_renders.json")
    if target.exists():
        previous = json.loads(target.read_text(encoding="utf-8"))
        if previous.get("source_sha256") != manifest["source_sha256"]:
            parser.error("该模型标识已用于其他模型，未覆盖。")
    # Keep existing public render locations; copy only validated derived PNGs
    # when importing results from outside the study or from ignored test storage.
    is_public_source = source.is_relative_to(study) and "IGNORE" not in source.parts
    paths = [manifest["neutral"]] + [r["path"] for r in manifest["expressions"]]
    translated = {}
    for relative in paths:
        image_path = (source / relative).resolve()
        if not image_path.is_relative_to(source):
            raise ValueError("渲染清单图片路径越界。")
        with Image.open(image_path) as image:
            image.load()
            if image.size != (512, 512) or not image.convert("RGBA").getchannel("A").getbbox():
                raise ValueError("图片尺寸错误或全透明：" + str(image_path))
        record = next((r for r in manifest["expressions"] if r["path"] == relative), None)
        if record and hashlib.sha256(image_path.read_bytes()).hexdigest() != record["sha256"]:
            raise ValueError("图片哈希与已验证清单不同：" + relative)
        if is_public_source:
            translated[relative] = image_path.relative_to(study).as_posix()
        else:
            destination = study / "images" / args.key / image_path.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists() and destination.read_bytes() != image_path.read_bytes():
                raise ValueError("目标图片已存在不同内容：" + str(destination))
            if not destination.exists():
                shutil.copy2(image_path, destination)
            translated[relative] = destination.relative_to(study).as_posix()
    adapter = {
        "collection": args.label, "armature": manifest["armature"],
        "mesh": " / ".join(manifest["meshes"]), "head_bone": manifest["camera"]["bone"],
        "head_world": manifest["camera"]["head_position"],
        "camera_location": manifest["camera"]["camera_location"],
        "camera_target": manifest["camera"]["target"],
        "orthographic_scale": manifest["camera"]["orthographic_scale"],
        "folder": args.key, "neutral": translated[manifest["neutral"]],
        "morph_driver": "mmd_tools_bound_sliders",
        "source_control_names": [r["name"] for r in manifest["all_morphs"]],
        "source_morph_types": manifest["type_counts"],
        "source_filename": manifest["source_filename"],
        "source_sha256": manifest["source_sha256"],
        "material_profile": manifest["material_profile"], "credit": args.credit,
        "expressions": [{**r, "path": translated[r["path"]]} for r in manifest["expressions"]],
        "seconds": manifest["seconds"],
    }
    target.write_text(json.dumps(adapter, ensure_ascii=False, indent=2), encoding="utf-8")
    subprocess.run([sys.executable, str(study / "scripts/build_reference.py")], check=True)
    print(json.dumps({"registered": args.label, "controls": len(adapter["expressions"]), "adapter": str(target)}, ensure_ascii=False))


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    main()
