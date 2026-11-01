# 从 PMX 到全部表情参考图

[返回仓库导航](../README.md) · [表情研究主表](../mmd表情调查/MMD表情参考.md) · [skill 源码](../skills/mmd-expression-reference/SKILL.md)

## 文件放哪里

```text
HoResearch/
├── IGNORE/                         # 整个目录不进入 Git / GitHub
│   ├── models/
│   │   ├── mmd-expression-study/   # 已移入的原工程和 Blender 备份
│   │   └── 新模型/                 # PMX / PMD 与它原有的贴图目录
│   ├── config/                    # 仅本机使用的 Blender / 插件路径
│   ├── runs/                      # 导入后打包的工作工程、任务参数与日志
│   └── tests/                     # 管线测试结果，不作为正式研究发布
├── skills/mmd-expression-reference/
│   ├── SKILL.md
│   ├── references/pipeline.md
│   └── scripts/                   # 通用导入、渲染与报告脚本
└── mmd表情调查/
    ├── MMD表情参考.md              # 已整理的跨模型研究主表
    └── 模型参考/新模型标识/         # 新模型的正式图片与单模型报告
```

原模型包、原始贴图、Blender 工程和自动备份只在本机保留。公开仓库只包含研究说明、渲染结果、名称/统计清单和流程代码。`IGNORE/` 由根 `.gitignore` 整体排除，`.pmx`、`.pmd`、`.blend` 另有兜底规则。

将模型放进 `IGNORE/models/` 时，连同它依赖的贴图保持相对目录结构。也可以只读导入仓库外部的模型，不需要把整个外部父目录复制进来。

## 一次完整流程

1. **检查输入**：确认 PMX/PMD 与贴图可读，启动独立的后台 Blender；不影响正在打开的 Blender 工程。
2. **导入**：使用本机 mmd_tools 导入网格、骨架、显示项和 morph；默认不导入物理模拟。
3. **绑定与替换材质**：绑定 group / vertex / bone / UV / material 的统一 morph 控制滑块，替换为参考用的 EEVEE Reference Toon，保留原纹理连接和 morph 驱动。
4. **自动取景并预览**：优先寻找 `頭` 或骨骼的 MMD 日文名；眼骨确定正面，脸部材质或头部权重确定范围，先生成基准、眨眼和张嘴等样张。
5. **渲染全部**：确认构图后，每次只启用一个控制滑块，值为 1，其余为 0；按源 morph 完整清单输出。默认 512×512 PNG、128 采样、透明背景、正交机位。
6. **整理核验**：核对源 morph 数量、图片解码、分辨率、透明图、哈希和基准差异；生成标准 Markdown 缩略图索引，并附 lil 完整统计的频率降序对照。

基准图、每个原始 morph 和零变化项目都保留。材质、衣服或牙齿键在当前头部取景下可能不明显；这类项目会标注，不能因为没有变化就跳过。另补组合辅助图时写明所有启用的键和权重。

## 以后直接交给 Codex

将 skill 安装后，可以直接说：

> 使用 $mmd-expression-reference 处理这个 PMX，自动导入、替换参考材质并渲染全部 512×512 表情。原始模型留在 IGNORE。

本仓库的 skill 已包含可执行脚本，不依赖某个固定模型的对象名。个人 skill 目录可使用指向 `skills/mmd-expression-reference` 的目录联接，保持安装版与仓库源码一致；复制安装时运行脚本需用 `--repo` 指定研究仓库。

## 也可以直接运行

在仓库根目录执行：

```powershell
python -m pip install -r ".\skills\mmd-expression-reference\scripts\requirements.txt"

# 先看预览
python ".\skills\mmd-expression-reference\scripts\run.py" `
  --pmx ".\IGNORE\models\新模型\model.pmx" --preview

# 确认构图，再执行全部；已校验的同任务图片可续渲染
python ".\skills\mmd-expression-reference\scripts\run.py" `
  --pmx ".\IGNORE\models\新模型\model.pmx" --all
```

无 `--preview` 参数时默认渲染全部。输出目录默认根据模型名称和 PMX 内容哈希生成，避免同名模型互相覆盖。`--output` 可指定输出目录；`--head-bone`、`--ortho-scale`、`--target-offset` 可校正特殊模型的头骨与机位。更改渲染设置需要使用新输出目录，不能混用旧图片。

本机路径配置见 [技术说明](../skills/mmd-expression-reference/references/pipeline.md)。自动探测不可用时，在 `IGNORE/config/mmd-expression-reference.local.json` 设置 `blender` 和 `mmd_addons`，配置不会进入公开仓库。

## 输出内容与验证

- `参考表.md`：基准图、全部实际 morph 的单项图片及 lil 全部统计对照。
- `images/`：正式 PNG；`thumbnails/`：用于 Markdown 的实际缩略图。
- `manifest.json`：源文件名与哈希、Blender / 插件版本、实际材质方案、头骨与机位、完整 morph 名称与类型、逐图哈希、完成状态和低变化项。
- `IGNORE/runs/<模型标识>/working.blend`：含原始贴图的打包工作工程，只用于本机复现。

只有完整渲染数量与源 morph 数量一致、所有图片核验通过时，`complete` 才为真。预览与中断任务不算完成。源纹理、程序版本、管线代码或参数变化时，签名不一致会阻止复用旧结果。

## 材质方案的边界

当前自动替换使用 **EEVEE Reference Toon**，不是 HoToonBSDF。它保留 MMD 的基础纹理、漫反射和透明度输入及相关驱动，但不复刻球贴图、toon 贴图与高光。没有真实 HoToon 节点/材质库时不会冒称 HoToon；若后续明确指定 HoToon，再接入并测试真实材质。

## 本机验证记录

2026-11-01，使用 Blender 4.5.8 LTS 与 mmd_tools 4.1.0：

- 从真实 PMX 重新导入 Appearance Miku，完成全部 45 个 morph 与基准图，核验通过。
- 在仅本机保留的测试副本中增加 group、bone、UV 和 material morph，与原有 vertex morph 一起完成 49 项全量渲染；五类都确认有实际画面变化。
- 输出为 512×512 PNG，预览不标记为完整；源模型、测试模型、纹理和打包工作工程均未放入可提交目录。

这说明当前默认管线已做真实导入与渲染验证，不代表任意第三方模型或未配置的 HoToon 材质都已验证兼容。
