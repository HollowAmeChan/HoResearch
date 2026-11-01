"""Validate rendered MMD images and create portable Markdown indexes."""
import argparse
from collections import Counter
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote

from PIL import Image, ImageChops


def safe_cell(text):
    return str(text).replace("|", "&#124;").replace("\n", " ")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--statistics", type=Path)
    args = parser.parse_args()
    root = args.output.resolve()
    manifest_path = root / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    base = Image.open(root / manifest["neutral"]).convert("RGBA")
    records = [{"name": "基准", "path": manifest["neutral"]}] + manifest["expressions"]
    errors = []
    for record in records:
        path = root / record["path"]
        with Image.open(path) as source:
            source.load()
            image = source.convert("RGBA")
            if image.size != (manifest["settings"]["size"],) * 2 or not image.getchannel("A").getbbox():
                errors.append(record["path"])
            delta = ImageChops.difference(base, image)
            record["same_as_neutral"] = not any(channel.getbbox() for channel in delta.split())
            record["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    manifest["validation_errors"] = errors
    if manifest["complete"] and len(manifest["expressions"]) != manifest["source_morph_count"]:
        raise RuntimeError("完整渲染的 morph 数量不匹配。")
    if errors:
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        raise RuntimeError("渲染图片为空或尺寸不符：" + ", ".join(errors))
    def picture(record):
        path = root / record["path"]
        thumb = root / "thumbnails" / path.name
        thumb.parent.mkdir(exist_ok=True)
        with Image.open(path) as image:
            image.thumbnail((160, 160), Image.Resampling.LANCZOS)
            image.save(thumb)
        label = safe_cell(record["name"]).replace("[", "\\[").replace("]", "\\]")
        return f"[![{label}]({quote(thumb.relative_to(root).as_posix(), safe='/')})]({quote(record['path'], safe='/')})"
    rows = [
        "# MMD 模型表情参考", "",
        f"- 输入：`{manifest['source_filename']}`；SHA-256：`{manifest['source_sha256']}`。",
        f"- 状态：{'全部完成' if manifest['complete'] else '预览，尚未渲染全部表情'}；源 morph：{manifest['source_morph_count']}；已渲染：{len(manifest['expressions'])}。",
        f"- 引擎：EEVEE；尺寸：{manifest['settings']['size']} × {manifest['settings']['size']}；采样：{manifest['settings']['samples']}。",
        f"- 头骨：`{manifest['camera']['bone']}`；材质方案：`{manifest['material_profile']}`。",
        "- 材质是统一 Reference Toon，不是 HoToon；未复刻 MMD 球贴图、toon 贴图和高光。",
        "- 原模型、原始贴图和打包工作工程只保存在本机，不包含在本报告目录。",
        "- 每张图只启用目标 MMD 控制滑块，权重为 1；网格、骨骼、材质、UV、组合驱动保留。",
        "", "## 无表情基准", "", picture(records[0]), "",
        "## 全部实际 morph", "",
        "| 序号 | 原始名称 | 类型 | 参考图 | 说明 |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for record in manifest["expressions"]:
        note = "与基准相同；可能需要基础表情或位于镜头外，待核对" if record["same_as_neutral"] else ""
        rows.append(f"| {record['index']} | {safe_cell(record['name'])} | {record['type']} | {picture(record)} | {note} |")
    if args.statistics and args.statistics.is_file():
        stats = []
        for line in args.statistics.read_text(encoding="utf-8-sig").splitlines():
            m = re.fullmatch(r"(.*):\s*([0-9.]+)\s*%\s*", line)
            if m:
                stats.append((m[1], m[2]))
            elif line.strip():
                raise ValueError("无法解析 lil 统计：" + line)
        stats.sort(key=lambda item: -Decimal(item[1]))
        by_name = {r["name"]: r for r in manifest["expressions"]}
        rows += ["", f"## lil 完整统计对照（{len(stats)} 项，使用率降序）", "",
                 "| 排名 | 统计原名 | 动作使用率 | 同名参考图 |",
                 "| ---: | --- | ---: | --- |"]
        for rank, (name, rate) in enumerate(stats, 1):
            record = by_name.get(name)
            image = picture(record) if record else "未找到完全同名项" if manifest["complete"] else "预览尚未覆盖"
            rows.append(f"| {rank} | {safe_cell(name)} | {rate} % | {image} |")
    rows += ["", "## 核验", "",
             f"- 已核验 {len(records)} 张 PNG 可解码、尺寸正确、不是全透明图。",
             "- `manifest.json` 保存全部源 morph、类型、机位、逐图 SHA-256 和完成状态。", ""]
    (root / "参考表.md").write_text("\n".join(rows), encoding="utf-8")
    manifest["type_counts"] = dict(Counter(m["type"] for m in manifest["all_morphs"]))
    manifest["low_change"] = [r["name"] for r in manifest["expressions"] if r["same_as_neutral"]]
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Report: {root / '参考表.md'}")


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    main()
