# MMD 表情调查

[返回研究导航](../README.md)

新模型的标准处理方式见 [PMX 自动导入与全表情渲染流程](../docs/MMD表情参考流程.md)，可使用 [mmd-expression-reference skill](../skills/mmd-expression-reference/SKILL.md)。

## 研究范围

以 lilxyzw 完整统计中的 **245 个原始表情名称**建立视觉参考，按动作使用率从高到低排列，并对照 HoTools 的现有预设与实际模型，再验证预设是否足够。同频时保持源文件顺序，名称变体不合并，全部模型未找到的项目也保留。

当前主表包含 **245 项统计名称**，逐项标记是否属于现有 **55 项 HoTools 预设**，对照 **4 个模型**：Sour 式初音、YYB 式初音、Appearance Miku、TDA 式初音。共 **275 张单项图 + 4 张基准图 + 8 张组合辅助图**，正式 PNG 均为 **512 × 512**。预设覆盖范围和表情语义尚待后续验证。

## 资料导航

| 资料 | 内容 |
| --- | --- |
| [MMD 表情参考主表](MMD表情参考.md) | lil 全部 245 项按使用率降序跨模型对照，标注 HoTools 预设、缺失项和候选命名变体 |
| [Sour 式初音全部明细](模型明细/01_Sour.md) | 94 个实际形态键及组合辅助示例 |
| [YYB 式初音全部明细](模型明细/02_YYB.md) | 73 个实际形态键 |
| [Appearance Miku 全部明细](模型明细/03_Appearance.md) | 45 个实际形态键 |
| [TDA 式初音全部明细](模型明细/04_TDA.md) | 63 个实际形态键及组合辅助示例 |
| [模型基准总览](模型基准总览.png) | 4 个模型的无表情机位对照 |
| [lilxyzw 表情统计附录](附录/lil_MMD表情统计.md) | 245 项动作使用率、38 项精选名称及原始统计口径 |
| [lil 统计与模型名称对应](lil统计与模型对应.csv) | 245 × 4 项统计名称匹配，按使用率降序排列 |
| [预设与模型名称对应](预设与模型对应.csv) | 55 × 4 项名称匹配与图片路径 |
| [工程检查记录](scene_inventory.json) | 集合、骨架、形态键、材质与贴图清单 |
| [渲染核验记录](render_validation.json) | 图片尺寸、SHA-256、画面差异与低变化项目 |
| [HoTools 目录快照](附录/HoTools_shapekey_catalog.csv) | 本次生成参考表所用的插件预设来源 |

`images/` 保存正式图片与各模型总览，`images/thumbnails/` 保存文档使用的缩略图，`质检/` 保存额外的抽样检查图片。`0*_renders.json` 保存模型机位、原始键名、组合条件及图片相对路径。

参考表采用标准 Markdown 图片语法，表内显示实际生成的小图，点击可打开 512 × 512 原图。无需依赖 HTML 的 `<img width="…">` 或 `<br>` 支持。重新生成文档时会自动检查表格列数。

## 实验条件与来源

- 整理日期：2026-11-01。
- 输入工程：原始本机文件 `mmd表情研究.blend`，现存于 `IGNORE/models/mmd-expression-study/`，未纳入 Git。原始检查记录中的旧绝对路径保留作来源信息。
- 渲染环境：Blender 4.5.11 LTS，EEVEE，128 采样。各模型按“頭”骨定位正面头部机位，同一模型保持机位和灯光一致。
- 单项图：目标形态键值为 1，其余为 0。组合辅助图的条件和两个键的权重单独标注。
- 原始文件保存的主要材质使用 `MMDShaderDev` 等节点组，沿用现有材质渲染。
- 外部统计来源：[lilxyzw 的 Gist](https://gist.github.com/lilxyzw/80608d9b16bf3458c61dec6b090805c5)。原文、元数据与版本快照保存在 `附录/` 中。
- 外部统计反映作者 483 个动作文件中的使用率，不代表模型拥有率。

## 复现方法

以下命令在仓库根目录执行。脚本根据自身位置定位本专题目录，不再依赖原来的文档目录。

### 只重新整理表格与核验

已有渲染图片和 JSON 清单时，使用普通 Python 即可：

```powershell
python -m pip install -r ".\mmd表情调查\scripts\requirements.txt"
python ".\mmd表情调查\scripts\build_reference.py"
```

该步骤会更新主表、模型明细、统计附录、总览、名称映射和图像核验记录。

脚本优先使用本机中文字体；可设置环境变量 `HORESEARCH_FONT` 指向兼容中文和日文的字体文件。

### 重新检查和渲染 Blender 工程

需要自行提供原始 `.blend` 工程，并设置 Blender 可执行文件路径。脚本内的模型、集合、骨架和材质名称对应本次原始工程，换模型时需相应调整。

```powershell
$blenderExe = "你的 Blender 安装目录\blender.exe"
$sourceBlend = "你的工程目录\mmd表情研究.blend"

& $blenderExe -b $sourceBlend --python-exit-code 1 --python ".\mmd表情调查\scripts\inspect_scene.py"
& $blenderExe -b $sourceBlend --python-exit-code 1 --python ".\mmd表情调查\scripts\render_expressions.py" -- --all
& $blenderExe -b $sourceBlend --python-exit-code 1 --python ".\mmd表情调查\scripts\render_expressions.py" -- --contexts
python ".\mmd表情调查\scripts\build_reference.py"
```

`--all` 会跳过已存在的单项图片。需要完全重渲时，先备份并移走相应的 `images/模型目录/`，再执行渲染命令。基准图和组合辅助图会重新生成。运行日志为本地产物，默认不提交。

## 后续验证

- 逐项确认候选命名变体是否与预设表达相同含义。
- 核对左右约定、需要基础表情的组合键，以及头部画面变化很小的项目。
- 结合实际模型表现与外部动作使用统计，评估是否补充或调整预设。
- 将确认结果与取舍依据记录下来，再修改 HoTools 的预设目录。
