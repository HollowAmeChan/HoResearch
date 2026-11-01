"""Extract a model ZIP into Git-ignored local storage, retaining legacy names."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
import re
import shutil
import stat
import subprocess
import sys
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--label")
    parser.add_argument("--filename-encoding", default="cp932")
    parser.add_argument("--password-env")
    parser.add_argument("--password-encoding", default="utf-8")
    parser.add_argument("--max-expanded-mib", type=int, default=4096)
    args = parser.parse_args()
    repo = args.repo.resolve()
    archive = args.archive.resolve()
    if not archive.is_file():
        parser.error("压缩包不存在。")
    ignored = subprocess.run(["git", "-C", str(repo), "check-ignore", "-q", "--", "IGNORE/models/check"], capture_output=True)
    if ignored.returncode != 0:
        parser.error("仓库必须先将 IGNORE/ 整体加入 .gitignore。")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    label = args.label or re.sub(r'[<>:"/\\|?*\s]+', "_", archive.stem)[:48] + "_" + digest[:8]
    if label in {"", ".", ".."} or re.search(r'[<>:"/\\|?*]', label):
        parser.error("--label 必须是单个合法目录名。")
    target = repo / "IGNORE/models" / label
    password_text = os.environ.get(args.password_env) if args.password_env else None
    password = password_text.encode(args.password_encoding) if password_text is not None else None
    with zipfile.ZipFile(archive, metadata_encoding=args.filename_encoding) as bundle:
        entries = bundle.infolist()
        if sum(i.file_size for i in entries) > args.max_expanded_mib * 1024 * 1024:
            parser.error("预计解压体积超过限制，尚未写入文件。")
        if any(i.flag_bits & 1 for i in entries) and password is None:
            parser.error("此 ZIP 已加密。请查看作者附带的说明，使用 --password-env 提供已知口令。")
        # Check the actual password before creating the destination.
        encrypted = [i for i in entries if i.flag_bits & 1 and not i.is_dir() and i.file_size]
        if encrypted:
            with bundle.open(min(encrypted, key=lambda i: i.file_size), pwd=password) as stream:
                while stream.read(65536):
                    pass
        plan = []
        for entry in entries:
            name = entry.filename.replace("\\", "/")
            parts = PurePosixPath(name).parts
            if PureWindowsPath(name).drive or name.startswith("/") or ".." in parts or stat.S_ISLNK(entry.external_attr >> 16):
                raise ValueError("压缩包包含越界路径或符号链接：" + name)
            destination = (target / Path(*parts)).resolve()
            if not destination.is_relative_to(target.resolve()):
                raise ValueError("压缩包路径超出目标目录：" + name)
            plan.append((entry, destination))
        if target.exists():
            parser.error("目标目录已存在，未覆盖：" + str(target))
        target.mkdir(parents=True)
        manifest = {
            "source_archive": str(archive), "source_sha256": digest,
            "filename_encoding": args.filename_encoding,
            "password_encoding": args.password_encoding if encrypted else None,
            "complete": False, "files": [],
        }
        manifest_path = target / "extraction_manifest.json"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        for entry, destination in plan:
            if entry.is_dir():
                destination.mkdir(parents=True, exist_ok=True)
                continue
            destination.parent.mkdir(parents=True, exist_ok=True)
            with bundle.open(entry, pwd=password) as source, destination.open("xb") as output:
                # ZipExtFile verifies CRC at EOF; do not extract twice just to test.
                shutil.copyfileobj(source, output, length=1024 * 1024)
            manifest["files"].append({"path": destination.relative_to(target).as_posix(), "size": entry.file_size, "crc32": f"{entry.CRC:08x}"})
            manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        manifest["complete"] = True
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    models = [str(p) for p in target.rglob("*") if p.suffix.lower() in {".pmx", ".pmd"}]
    print(json.dumps({"destination": str(target), "files": len(manifest["files"]), "crc_verified": True, "models": models}, ensure_ascii=False))


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    main()
