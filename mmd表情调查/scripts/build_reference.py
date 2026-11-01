"""Assemble Markdown, original-name mappings, statistics and visual QA."""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import sys
import unicodedata
from collections import Counter
from decimal import Decimal
from pathlib import Path
from urllib.parse import quote

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8")
OUT = Path(__file__).resolve().parents[1]
GIST_URL = "https://gist.github.com/lilxyzw/80608d9b16bf3458c61dec6b090805c5"


def load_label_font():
    """Use an explicit font or a local CJK font without hardcoding a user path."""
    candidates = [
        os.environ.get("HORESEARCH_FONT"),
        str(Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts" / "msyh.ttc"),
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/System/Library/Fonts/PingFang.ttc",
    ]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            return ImageFont.truetype(candidate, 18)
        except OSError:
            continue
    raise RuntimeError("找不到中日文字体；请将 HORESEARCH_FONT 设置为可用字体文件的路径。")


FONT = load_label_font()


def dump_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def cell(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def write_markdown(path, lines):
    """Reject malformed pipe tables before replacing a generated document."""
    text = "\n".join(lines)
    table = []
    for number, line in enumerate(text.splitlines() + [""], 1):
        if line.startswith("|") and line.endswith("|"):
            table.append((number, line.strip("|").split("|")))
            continue
        if not table:
            continue
        expected = len(table[0][1])
        if len(table) < 2 or not all(re.fullmatch(r"\s*:?-{3,}:?\s*", c) for c in table[1][1]):
            raise ValueError(f"{path.name}:{table[0][0]} 表格缺少合法分隔行")
        for row_number, columns in table:
            if len(columns) != expected:
                raise ValueError(f"{path.name}:{row_number} 表格应为 {expected} 列，实际 {len(columns)} 列")
        table = []
    path.write_text(text, encoding="utf-8")


def normalized(value):
    return unicodedata.normalize("NFKC", value).strip()


def image_tag(path, label, width=144, prefix=""):
    """Use real thumbnails and standard Markdown, including inside table cells."""
    digest = hashlib.sha256(path.encode("utf-8")).hexdigest()[:16]
    thumbnail = f"images/thumbnails/{width}/{digest}.png"
    target = OUT / thumbnail
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(OUT / path) as source:
        image = source.convert("RGBA")
        image.thumbnail((width, width), Image.Resampling.LANCZOS)
        image.save(target)
    alt = cell(label).replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")
    full_url = quote(prefix + path, safe="/")
    thumbnail_url = prefix + thumbnail
    return f"[![{alt}]({thumbnail_url})]({full_url})"


def read_data():
    with (OUT / "附录" / "HoTools_shapekey_catalog.csv").open(encoding="utf-8-sig", newline="") as f:
        presets = [r for r in csv.DictReader(f) if r["standard"] == "MMD" and r["role"] == "TEMPLATE"]
    inventory = json.loads((OUT / "scene_inventory.json").read_text(encoding="utf-8"))
    paths = [p for p in OUT.glob("*_renders.json") if re.match(r"^\d+_", p.name)]
    paths.sort(key=lambda p: (int(p.name.split("_", 1)[0]), p.name))
    models = [json.loads(p.read_text(encoding="utf-8")) for p in paths]
    return presets, inventory, models


def statistics(presets):
    root = OUT / "附录"
    snap = json.loads((root / "lilxyzw_gist_snapshot.json").read_text(encoding="utf-8-sig"))
    curated = [s.strip() for s in (root / "mmd_morph_names.txt").read_text(encoding="utf-8-sig").splitlines() if s.strip()]
    rates = {}
    for line in (root / "mmd_morph_names_all.txt").read_text(encoding="utf-8-sig").splitlines():
        match = re.match(r"^(.*):\s*([0-9.]+)\s*%\s*$", line)
        if match:
            rates[match[1]] = match[2]
        elif line.strip():
            raise ValueError(f"Unparsed statistic: {line!r}")
    # Keep each original spelling as a separate row; ties retain source order.
    rates = dict(sorted(rates.items(), key=lambda item: -Decimal(item[1])))
    preset_names = {p["name"] for p in presets}
    lines = [
        "# 附录：lilxyzw 的 MMD 表情使用统计", "",
        f"- 原始来源：<{GIST_URL}>",
        "- 保存日期：2026-11-01（Asia/Shanghai）。",
        f"- Gist 版本：`{snap['history'][0]['version']}`。",
        f"- Gist 元数据更新时间：`{snap['updated_at']}`。",
        "- 样本为作者手头的 **483 个动作文件**。统计对象是动作中的 morph 使用率，不是模型拥有率。",
        "- 按作者说明，关键帧数量不超过 2，或全部关键帧权重不超过 0.01 的项目，被视为未使用并排除。",
        "- 精选清单来自较高使用率的项目，名称向 MMD 附带模型统一后进一步筛选。",
        "- 原始名称和百分比均保留；完整统计按数值从高到低排列，同频时保持源文件顺序，不合并全半角、大小写或名称变体。",
        "- “HoTools 预设”仅表示名称完全相同；不据此判定形态或左右语义完全一致。",
        "", "## 作者原文说明", "", "> " + snap["description"].replace("\n", "\n> "),
        "", "## 精选清单", "",
        "| 序号 | 原始名称 | 原始统计中的同名使用率 | HoTools 预设 |",
        "| ---: | --- | ---: | --- |",
    ]
    for i, name in enumerate(curated, 1):
        rate = rates.get(name)
        lines.append(f"| {i} | {cell(name)} | {rate + ' %' if rate else '无完全同名统计'} | {'是' if name in preset_names else '否'} |")
    lines += [
        "", f"## 完整统计（{len(rates)} 项）", "",
        "| 排名 | 原始 morph 名称 | 动作使用率 | 作者精选 | HoTools 预设 |",
        "| ---: | --- | ---: | --- | --- |",
    ]
    for i, (name, rate) in enumerate(rates.items(), 1):
        lines.append(f"| {i} | {cell(name)} | {rate} % | {'是' if name in curated else ''} | {'是' if name in preset_names else ''} |")
    lines += [
        "", "## 原始快照", "",
        "- [精选名称原文](mmd_morph_names.txt)",
        "- [完整统计原文](mmd_morph_names_all.txt)",
        "- [Gist 元数据与正文快照](lilxyzw_gist_snapshot.json)",
        "- [本次 HoTools 目录快照](HoTools_shapekey_catalog.csv)", "",
    ]
    write_markdown(root / "lil_MMD表情统计.md", lines)
    return rates, curated


def match_preset(name, model):
    expressions = model["expressions"]
    for item in expressions:
        if item["name"] == name:
            return "完全同名", item
    matches = [item for item in expressions if normalized(item["name"]) == normalized(name)]
    if len(matches) == 1:
        return "全半角兼容", matches[0]
    # Keep author-specific variants explicit; never count as exact coverage.
    candidates = [name + "E", "x" + name]
    for candidate in candidates:
        matches = [item for item in expressions if normalized(item["name"]) == normalized(candidate)]
        if len(matches) == 1:
            return "候选变体", matches[0]
    return "未找到", None


def check_images(models, inventory):
    issues = []
    image_records = []
    unchanged = []
    total = 0
    for model in models:
        expected = len(model["source_control_names"]) if "source_control_names" in model else len([n for n in model["source_shape_key_names"] if n not in {"Basis"} and not n.startswith("mmd_sdef_")])
        if len(model["expressions"]) != expected:
            issues.append(f"{model['collection']}: expected {expected}, got {len(model['expressions'])}")
        base = np.array(Image.open(OUT / model["neutral"]).convert("RGBA"), dtype=np.int16)
        all_items = [{"name": "基准", "path": model["neutral"]}] + model["expressions"] + model.get("context_examples", [])
        for item in all_items:
            path = OUT / item["path"]
            if not path.exists():
                issues.append(f"Missing {item['path']}")
                continue
            im = Image.open(path)
            im.verify()
            with Image.open(path) as im:
                rgba = np.array(im.convert("RGBA"), dtype=np.int16)
                if im.size != (512, 512):
                    issues.append(f"Bad size {path.name}: {im.size}")
            if int(np.count_nonzero(rgba[:, :, 3])) < 512:
                issues.append(f"Empty image {path.name}")
            comparison = base
            if "baseline_path" in item:
                comparison = np.array(Image.open(OUT / item["baseline_path"]).convert("RGBA"), dtype=np.int16)
            delta = np.abs(rgba - comparison)
            changed = np.max(delta, axis=2) > 8
            changed_count = int(np.count_nonzero(changed))
            rec = {
                "model": model["collection"], "name": item["name"],
                "path": item["path"], "size": [512, 512],
                "comparison": item.get("baseline_path", model["neutral"]),
                "changed_pixels_vs_comparison_over_8": changed_count,
                "mean_absolute_delta": round(float(delta.mean()), 6),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
            image_records.append(rec)
            if item["name"] != "基准" and "context_weights" not in item and changed_count < 32:
                unchanged.append(rec)
            total += 1
    dump_json(OUT / "render_validation.json", {
        "issues": issues, "total_images": total,
        "expressions": sum(len(m["expressions"]) for m in models),
        "neutral_images": len(models), "low_visual_change": unchanged,
        "context_examples": sum(len(m.get("context_examples", [])) for m in models),
        "images": image_records,
    })
    if issues:
        raise RuntimeError("\n".join(issues))
    return image_records, unchanged


def neutral_overview(models):
    width = 512 * len(models)
    canvas = Image.new("RGB", (width, 550), "#eeeeee")
    draw = ImageDraw.Draw(canvas)
    for i, model in enumerate(models):
        im = Image.open(OUT / model["neutral"]).convert("RGBA")
        background = Image.new("RGBA", im.size, "#eeeeee")
        background.alpha_composite(im)
        canvas.paste(background.convert("RGB"), (i * 512, 38))
        draw.text((i * 512 + 12, 8), model["collection"], font=FONT, fill="#222222")
    canvas.save(OUT / "模型基准总览.png")


def contact_sheet(model):
    entries = [{"name": "基准", "path": model["neutral"]}] + model["expressions"]
    tile = 164
    cols = 7
    height = 190
    canvas = Image.new("RGB", (cols * tile, ((len(entries) + cols - 1) // cols) * height), "#eeeeee")
    draw = ImageDraw.Draw(canvas)
    for i, entry in enumerate(entries):
        im = Image.open(OUT / entry["path"]).convert("RGBA")
        im.thumbnail((160, 160), Image.Resampling.LANCZOS)
        bg = Image.new("RGBA", im.size, "#eeeeee")
        bg.alpha_composite(im)
        x = i % cols * tile
        y = i // cols * height
        canvas.paste(bg.convert("RGB"), (x + 2, y))
        label = f"{i:03d} {entry['name']}"
        draw.text((x + 4, y + 163), label[:18], font=FONT, fill="#222222")
    name = f"{model['folder']}_总览.jpg"
    canvas.save(OUT / "images" / name, quality=92)
    return "images/" + name


def build():
    presets, inventory, models = read_data()
    rates, curated = statistics(presets)
    records, low_change = check_images(models, inventory)
    context_count = sum(len(m.get("context_examples", [])) for m in models)
    context_differences = {r["path"]: r["changed_pixels_vs_comparison_over_8"] for r in records if "/context_" in r["path"]}
    low_lookup = {(r["model"], r["name"]): r for r in low_change}
    neutral_overview(models)
    report_dir = OUT / "模型明细"
    report_dir.mkdir(exist_ok=True)
    preset_mapping = []
    for i, preset in enumerate(presets, 1):
        for model in models:
            status, item = match_preset(preset["name"], model)
            preset_mapping.append({
                "preset_index": i, "preset": preset["name"],
                "region": preset["region"], "model": model["collection"],
                "match_type": status, "actual_shape_key": item["name"] if item else "",
                "image": item["path"] if item else "",
            })
    with (OUT / "预设与模型对应.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(preset_mapping[0]))
        writer.writeheader()
        writer.writerows(preset_mapping)
    preset_names = {preset["name"] for preset in presets}
    mapping = []
    used = {m["collection"]: set() for m in models}
    for rank, (name, rate) in enumerate(rates.items(), 1):
        for model in models:
            status, item = match_preset(name, model)
            if item:
                used[model["collection"]].add(item["name"])
            mapping.append({
                "rank": rank, "statistic_name": name, "usage_percent": rate,
                "hotools_preset": "是" if name in preset_names else "否",
                "model": model["collection"], "match_type": status,
                "actual_shape_key": item["name"] if item else "",
                "image": item["path"] if item else "",
            })
    with (OUT / "lil统计与模型对应.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(mapping[0]))
        writer.writeheader()
        writer.writerows(mapping)
    lines = [
        "# MMD 表情参考", "",
        "- 制作日期：2026-11-01（Asia/Shanghai）。",
        ("- 历史四模型来源：原 `mmd表情研究.blend` 工程；新增模型由 PMX 独立导入。原件及打包工作工程均保存在本机 `IGNORE/`。" if any(m.get("morph_driver") for m in models) else "- 当前模型来源：原 `mmd表情研究.blend` 工程；原件保存在本机 `IGNORE/`。"),
        f"- 主表以 lilxyzw 完整统计中的 **{len(rates)} 个原始表情名称**为准，按动作使用率从高到低排列；同频保持源文件顺序。",
        "- HoTools 的 **55 条 MMD TEMPLATE** 仅作为预设对照列，未收录的统计名称也全部保留。",
        f"- 本次输出：**{sum(len(m['expressions']) for m in models)} 张单项表情/控制图 + {len(models)} 张基准图 + {context_count} 张组合辅助图**，全部为 **512 × 512 PNG**。",
        f"- {len(models)} 个模型均以各自骨架的 **“頭”骨**定位，结合眼骨朝向与脸部材质包围盒确定正面正交机位。",
        "- 每次只激活一个实际形态键（值 1.0），其余归零。同一模型的机位、灯光和取景固定；128 渲染采样，透明背景。",
        "- 牙齿和特殊眼的组合辅助图另行启用一个基础键，**两个键均为 1.0**；图片明确标注组合，不与单项图混淆。",
        ("- 历史四模型沿用工程中的 `MMDShaderDev` 等原材质；新增自动导入模型使用 EEVEE Reference Toon，方案见各模型明细。材质差异不能直接视为表情差异。" if any(m.get("morph_driver") for m in models) else "- 当前模型沿用工程中的 `MMDShaderDev` 等原材质，方案见各模型明细。"),
        ("- 原工程以实际形态键驱动；新增模型通过 mmd_tools 绑定的完整 morph 滑块驱动，保留材质、骨骼、UV 与组合类型。" if any(m.get("morph_driver") for m in models) else "- 当前列按原工程的实际网格形态键驱动与统计，完整 PMX morph 覆盖需另行核验。"),
        "- `Basis` 和 `mmd_sdef_c / mmd_sdef_r0 / mmd_sdef_r1` 是基准/辅助数据，不当作表情渲染。",
        "- 模型原有的换装、附件、局部调节键同样保留独立渲染，放入模型明细；头部取景下可能没有明显差异。",
        "- 此版本用于完整统计与实际模型的视觉对照，暂不据此宣称预设完整，也不修改插件中的预设。",
        "", "## 阅读方式", "",
        "- 表内使用标准 Markdown 缩略图链接；点击缩略图可打开 512 × 512 原图。缩略图单独保存在 `images/thumbnails/`。",
        "- **完全同名**：主表默认直接展示图片。",
        "- **全半角兼容**：仅统一 Unicode 全半角；图片旁注明原始键名。",
        "- **候选变体**：仅明确列出 `x` 前缀或 `E` 后缀的作者变体，供视觉研究；不计入完全同名覆盖，不据名称断言等价。",
        "- **未找到**：该模型没有对应键，也没有采用上述候选命名。不会生成一张基准图冒充该表情。",
        "- **HoTools 预设**：仅当该统计原名与现有 TEMPLATE 完全同名时标记“是”；不据此合并统计中的名称变体。",
        f"- lil 的原始名称、全半角、大小写及频率精度全部保留；即使 {len(models)} 个模型都未找到图片，该行也会保留。",
        "- lil 使用率是 **483 个动作中的使用率**，不是模型拥有率；下方汇总为统计名称的匹配情况，不直接等同功能覆盖率。",
        "", "## 模型与统计名称对应", "",
        "| 模型集合 | 骨架 | 单项控制图 | 完全同名 | 全半角兼容 | 候选变体 | 未找到 | 全部原名与图片 |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for model in models:
        counts = Counter(r["match_type"] for r in mapping if r["model"] == model["collection"])
        detail = f"模型明细/{model['folder']}.md"
        lines.append(f"| {model['collection']} | {model['armature']} | {len(model['expressions'])} | {counts['完全同名']} | {counts['全半角兼容']} | {counts['候选变体']} | {counts['未找到']} | [模型明细]({quote(detail, safe='/')}) |")
    lines += [
        "", "## 无表情基准", "",
        "| " + " | ".join(m["collection"] for m in models) + " |",
        "| " + " | ".join("---" for _ in models) + " |",
        "| " + " | ".join(image_tag(m["neutral"], m["collection"] + " 基准", 220 if len(models) <= 4 else 160) for m in models) + " |",
        "", f"## lil 全部表情参考表（{len(rates)} 项，使用率降序）", "",
        "| 排名 | lil 统计原名 | 动作使用率 | HoTools 预设 | " + " | ".join(m["collection"] for m in models) + " |",
        "| ---: | --- | ---: | --- | " + " | ".join("---" for _ in models) + " |",
    ]
    for rank, (name, rate) in enumerate(rates.items(), 1):
        cells = [str(rank), cell(name), rate + " %", "是" if name in preset_names else "否"]
        for model in models:
            status, item = match_preset(name, model)
            if not item:
                cells.append("未找到")
                continue
            label = "" if status == "完全同名" else f" {status}：{cell(item['name'])}"
            low = "；头部画面变化很小，待核对" if (model["collection"], item["name"]) in low_lookup else ""
            combined = ""
            for example in model.get("context_examples", []):
                if example["name"] == item["name"]:
                    context_name = next(iter(example["context_weights"]))
                    combined += f"；[组合辅助：{cell(context_name)}=1 + {cell(item['name'])}=1]({quote(example['path'], safe='/')})"
                    if context_differences[example["path"]] < 32:
                        combined += "；组合中仍无明显可见变化，待核对"
            cells.append(image_tag(item["path"], model["collection"] + " " + item["name"]) + label + low + combined)
        lines.append("| " + " | ".join(cells) + " |")
    lines += [
        "", "## 模型独有项与全部渲染", "",
        "以下页面列出各模型**全部实际形态键或绑定 morph**，包括未出现在 lil 统计主表中的项目，方便下一轮交叉验证。", "",
    ]
    for model in models:
        overview = contact_sheet(model)
        details = [
            f"# {model['collection']}：全部表情/控制参考", "",
            "[返回预设主表](../MMD%E8%A1%A8%E6%83%85%E5%8F%82%E8%80%83.md)", "",
            f"- 骨架：`{model['armature']}`；定位骨：`頭`。",
            f"- 网格：`{model['mesh']}`。",
            f"- 全部 {len(model['expressions'])} 个{'MMD morph 控制滑块' if model.get('morph_driver') else '非辅助形态键'}均已单独渲染；PNG 为 512 × 512。",
            f"- 材质方案：`{model.get('material_profile', '工程原材质（MMDShaderDev 等）')}`。",
            *([f"- 制作来源署名：{model['credit']}。"] if model.get("credit") else []),
            *([f"- 源文件：`{model['source_filename']}`；SHA-256：`{model['source_sha256']}`。"] if model.get("source_filename") else []),
            "- 表内使用实际生成的 192 × 192 缩略图；点击缩略图可打开 512 × 512 原图。",
            f"- 主表以 lil 完整统计的 {len(rates)} 项为准，按使用率降序排列。“未用于主表”指未映射进统计主表，不表示该功能一定缺少预设。",
            "", "## 总览", "",
            f"![全部形态键总览](../{quote(overview, safe='/')})",
            "", "## 逐项图片", "",
            "| 序号 | 模型原始控制名 | 图片 | 主表关联 / 观察 |",
            "| ---: | --- | --- | --- |",
            f"| 000 | 基准（全部为 0） | {image_tag(model['neutral'], '基准', 192, '../')} | 无表情对照 |",
        ]
        for item in model["expressions"]:
            links = [r for r in mapping if r["model"] == model["collection"] and r["actual_shape_key"] == item["name"]]
            annotation = "；".join(f"#{r['rank']} {r['statistic_name']}（{r['match_type']}；{r['usage_percent']} %）" for r in links) or "未用于主表"
            if item.get("type"):
                annotation = f"{item['type']} morph；" + annotation
            if (model["collection"], item["name"]) in low_lookup:
                annotation += "；头部画面变化很小，待核对"
            details.append(f"| {item['index']:03d} | {cell(item['name'])} | {image_tag(item['path'], item['name'], 192, '../')} | {cell(annotation)} |")
        if model.get("context_examples"):
            details += [
                "", "## 组合辅助示例", "",
                "某些形态键作用于已有特殊眼或张嘴后的牙齿。以下保留单项图，并另补基础键对照与组合结果；未改变原始形态键。", "",
                "| 目标形态键 | 基础键对照（基础键 = 1） | 组合结果（基础键 = 1、目标键 = 1） | 权重 |",
                "| --- | --- | --- | --- |",
            ]
            for example in model["context_examples"]:
                context_name = next(iter(example["context_weights"]))
                note = "；组合中仍无明显可见变化，待核对" if context_differences[example["path"]] < 32 else ""
                details.append("| " + " | ".join((
                    cell(example["name"]),
                    image_tag(example["baseline_path"], context_name + "=1", 192, "../"),
                    image_tag(example["path"], example["name"] + " 组合", 192, "../"),
                    f"{cell(context_name)}=1；{cell(example['name'])}=1{note}",
                )) + " |")
        details.append("")
        write_markdown(report_dir / (model["folder"] + ".md"), details)
        extra_count = len(model["expressions"]) - len(used[model["collection"]])
        detail_path = quote("模型明细/" + model["folder"] + ".md", safe="/")
        lines.append(f"- [{model['collection']}：{len(model['expressions'])} 项全部图片]({detail_path})；其中 {extra_count} 项未用于主表。")
    lines += [
        "", "## 渲染核验", "",
        f"- 已检查 {len(records)} 张 PNG：文件可解码、尺寸全部为 512 × 512、图像不是全透明空图。",
        "- `render_validation.json` 保留逐图 SHA-256、相对基准的像素差异和低变化项目；组合辅助图与其基础键图比较。",
        f"- 有 {len(low_change)} 个项目在头部画面中变化很小，明细中已标注；这可能是换装/附件键、隐藏部件、微小调整或需进一步检查的项目。",
        "- 图像差异只用于排查空白/重复结果，不代替表情语义和模型制作正确性的人工判断。",
        "- 历史四模型工程在载入时曾报告一处原有骨约束依赖循环，原工程未作修复；新增 PMX 为独立后台导入，不沿用旧工程。",
        "", "## lil 统计附录", "",
        "- [lilxyzw 完整统计表、精选列表、样本与统计口径](%E9%99%84%E5%BD%95/lil_MMD%E8%A1%A8%E6%83%85%E7%BB%9F%E8%AE%A1.md)",
        f"- 原始 Gist：<{GIST_URL}>。",
        "- 原始 TXT、Gist JSON 快照和本次 HoTools 预设 CSV 都在 `附录` 中。",
        "", "## 可复现文件", "",
        "- `scripts/render_expressions.py`：Blender 批量渲染脚本。",
        "- `scripts/build_reference.py`：生成表格、明细与图像核验。",
        "- `scene_inventory.json`：集合、骨架、形态键、材质、贴图清单。",
        "- `0*_renders.json`：每个模型的镜头、实际键名和图片路径。",
        f"- `lil统计与模型对应.csv`：按使用率降序排列的 {len(rates)} × {len(models)} 项统计名称与图片映射。",
        f"- `预设与模型对应.csv`：按预设原始顺序排列的 {len(presets)} × {len(models)} 项名称映射。",
        "- `render_validation.json`：完整图像核验。",
        "- `render.log`：Blender 渲染日志。", "",
    ]
    write_markdown(OUT / "MMD表情参考.md", lines)
    print(json.dumps({
        "models": len(models), "presets": len(presets),
        "expression_images": sum(len(m["expressions"]) for m in models),
        "png_images": len(records), "lil_statistics": len(rates),
        "context_examples": context_count,
        "lil_curated": len(curated), "low_visual_change": len(low_change),
    }, ensure_ascii=False))


if __name__ == "__main__":
    build()
