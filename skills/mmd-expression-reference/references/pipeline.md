# 本机配置与实现边界

## 配置

本机设置存储在仓库根目录的 `IGNORE/config/mmd-expression-reference.local.json`，不提交：

```json
{
  "blender": "本机 Blender 安装目录/blender.exe",
  "mmd_addons": "包含 mmd_tools 文件夹的 addons 目录"
}
```

`run.py --help` 列出参数。可用 `--repo` 指定 HoResearch 根目录，`--blender`、`--mmd-addons` 覆盖自动探测。普通 Python 需要 Pillow；Blender 内使用它自带的 Python 和已安装的 mmd_tools。

原始模型放 `IGNORE/models/<模型>/`；导入并打包的工作工程、日志和任务参数存 `IGNORE/runs/<模型标识>/`。若输入位于仓库内且未被 Git 忽略，脚本拒绝执行，先将模型包移入 `IGNORE/`。外部输入只读，不擅自复制整个桌面或下载目录。

## 稳定的接口

### 日文 ZIP

`extract_zip.py` 支持嵌套包中选定的内层 ZIP、传统 ZIP 加密、CP932 文件名和可配置的口令编码。必须由使用者提供已有的正确口令；先核对作者说明和许可。口令用 `--password-env` 指定环境变量名称，日文旧工具生成的密码可用 `--password-encoding cp932`。UTF-8 标记的文件名仍由 ZIP 标记决定。

脚本保留原压缩包，拒绝覆盖现有解压目录、越界路径和符号链接。每个文件读取到 EOF 时校验 CRC，解压清单只存编码、大小、CRC 与来源哈希，不保存口令。部分解压失败时 `complete` 保持为假。

### Blender

- `bpy.ops.mmd_tools.import_model`：导入 MESH、ARMATURE、MORPHS、DISPLAY；不导入 PHYSICS，缩放默认 0.08，不合并重叠顶点。
- `mmd_tools.core.model.Model(root).morph_slider.bind()`：创建并绑定全类型控制滑块。placeholder 本身不渲染。
- 找骨骼时同时检查 Blender 名称和 `pose_bone.mmd_bone.name_j`；导入器可能将左右名称转换为 `.L/.R`。
- 眼骨朝向决定正面，头骨头尾决定上方向。脸部材质区域用于边界候选；失败时使用头骨及子骨权重的顶点，排除远离头部的长发。
- 材质适配保留外层 `mmd_shader` 节点、接口顺序、纹理链接及驱动；只替换共享 shader group 的内部实现。材质 morph 继续作用于同名输入。

## 当前替换方案

Reference Toon 使用 Diffuse → Shader to RGB → 两段明暗 → 漫反射/基础贴图颜色 → Emission，加独立透明混合。它是研究用统一显示，不复刻所有 MMD 球贴图、toon 贴图或高光效果；报告必须保留这个限制。原始 MMD 材质不在磁盘源模型中被修改。

真实 HoToon 节点/材质库未配置时，不自动伪造 HoToon 适配。新适配需验证透明睫毛、眼高光、口腔、材质 morph 和至少一个 UV/group/bone morph。

## 检验与续渲染

任务签名包含输入文件和纹理 SHA-256、Blender 版本与构建、mmd_tools 版本、管线代码哈希、材质方案、取景和渲染参数。首张图输出前先写任务签名；仅在签名一致且 PNG 可解码、尺寸正确时复用已有图。换模型或设置不会静默混用旧图。

manifest 包含完整源 morph 名称、分类、控制名称、逐项状态、尺寸、文件校验、机位和低变化提示。完整渲染必须核对 PMX 源 morph 数量与导入后的控制滑块数量。只完成预览不能标记为完整。

低变化可能是隐藏牙齿、依赖基础特殊眼、衣服切换或镜头外效果。保留单项图；补组合时明确写条件，不给没有的表情捏造参考图。
