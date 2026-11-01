# MMD 表情参考

- 制作日期：2026-11-01（Asia/Shanghai）。
- 源工程：`C:\Users\hhh12\Desktop\mmd表情研究.blend`；原始工程未覆盖保存。
- 预设来源：HoTools `ShapekeyTools/shapekey_catalog.csv` 中 MMD 的 **55 条 TEMPLATE**，顺序和名称保持原样。
- 本次输出：**275 张单项形态键图 + 4 张基准图 + 8 张组合辅助图**，全部为 **512 × 512 PNG**。
- 四个模型均以各自骨架的 **“頭”骨**定位，结合眼骨朝向与脸部材质包围盒确定正面正交机位。
- 每次只激活一个实际形态键（值 1.0），其余归零。同一模型的机位、灯光和取景固定；128 渲染采样，透明背景。
- 牙齿和特殊眼的组合辅助图另行启用一个基础键，**两个键均为 1.0**；图片明确标注组合，不与单项图混淆。
- 材质按工程磁盘保存状态原样使用。检查到的主要连接为 `MMDShaderDev` 等节点组，未检测到名含 `HoToon` 的节点；没有为此替换或重建材质。
- `Basis` 和 `mmd_sdef_c / mmd_sdef_r0 / mmd_sdef_r1` 是基准/辅助数据，不当作表情渲染。
- 模型原有的换装、附件、局部调节键同样保留独立渲染，放入模型明细；头部取景下可能没有明显差异。
- 此版本用于视觉对照，暂不据此宣称预设完整，也不修改插件中的预设。

## 阅读方式

- **完全同名**：主表默认直接展示图片。
- **全半角兼容**：仅统一 Unicode 全半角；图片旁注明原始键名。
- **候选变体**：仅明确列出 `x` 前缀或 `E` 后缀的作者变体，供视觉研究；不计入完全同名覆盖，不据名称断言等价。
- **未找到**：该模型没有对应键，也没有采用上述候选命名。不会生成一张基准图冒充该表情。
- 主表的“其他”沿用插件分类，包含眉形、瞳孔及特殊效果；不擅自重分类。
- lil 使用率按原统计中的完全同名项填写；这是 **483 个动作中的使用率**，不是模型覆盖率。

## 模型与预设覆盖

| 模型集合 | 骨架 | 实际形态键图 | 完全同名 | 全半角兼容 | 候选变体 | 未找到 | 全部原名与图片 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sour式初音 | Black_arm | 94 | 27 | 0 | 13 | 15 | [模型明细](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/01_Sour.md) |
| YYB式初音 | YYB Hatsune Miku default 1.0ver_arm | 73 | 29 | 0 | 6 | 20 | [模型明细](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/02_YYB.md) |
| Appearance Miku | Appearance Miku_arm | 45 | 25 | 0 | 0 | 30 | [模型明细](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/03_Appearance.md) |
| TDA式初音 | Tda式初音ミクV4X Ver1.00_arm | 63 | 48 | 0 | 0 | 7 | [模型明细](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/04_TDA.md) |

## 无表情基准

| Sour式初音 | YYB式初音 | Appearance Miku | TDA式初音 |
| --- | --- | --- | --- |
| <img src="images/01_Sour/000_%E5%9F%BA%E5%87%86.png" alt="Sour式初音 基准" width="220"> | <img src="images/02_YYB/000_%E5%9F%BA%E5%87%86.png" alt="YYB式初音 基准" width="220"> | <img src="images/03_Appearance/000_%E5%9F%BA%E5%87%86.png" alt="Appearance Miku 基准" width="220"> | <img src="images/04_TDA/000_%E5%9F%BA%E5%87%86.png" alt="TDA式初音 基准" width="220"> |

## 现有预设参考表

| # | 预设原名 | 插件区域 | lil 使用率 | Sour式初音 | YYB式初音 | Appearance Miku | TDA式初音 |
| ---: | --- | --- | ---: | --- | --- | --- | --- |
| 1 | まばたき | 眼部 | 87.57764 % | <img src="images/01_Sour/001_%E3%81%BE%E3%81%B0%E3%81%9F%E3%81%8D.png" alt="Sour式初音 まばたき" width="144"> | <img src="images/02_YYB/014_%E3%81%BE%E3%81%B0%E3%81%9F%E3%81%8D.png" alt="YYB式初音 まばたき" width="144"> | <img src="images/03_Appearance/016_%E3%81%BE%E3%81%B0%E3%81%9F%E3%81%8D.png" alt="Appearance Miku まばたき" width="144"> | <img src="images/04_TDA/001_%E3%81%BE%E3%81%B0%E3%81%9F%E3%81%8D.png" alt="TDA式初音 まばたき" width="144"> |
| 2 | 笑い | 眼部 | 68.73706 % | <img src="images/01_Sour/002_%E7%AC%91%E3%81%84.png" alt="Sour式初音 笑い" width="144"> | <img src="images/02_YYB/015_%E7%AC%91%E3%81%84.png" alt="YYB式初音 笑い" width="144"> | <img src="images/03_Appearance/017_%E7%AC%91%E3%81%84.png" alt="Appearance Miku 笑い" width="144"> | <img src="images/04_TDA/002_%E7%AC%91%E3%81%84.png" alt="TDA式初音 笑い" width="144"> |
| 3 | ウィンク | 眼部 | 27.12215 % | <img src="images/01_Sour/003_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF.png" alt="Sour式初音 ウィンク" width="144"> | <img src="images/02_YYB/016_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF.png" alt="YYB式初音 ウィンク" width="144"> | 未找到 | <img src="images/04_TDA/003_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF.png" alt="TDA式初音 ウィンク" width="144"> |
| 4 | ウィンク右 | 眼部 | 11.80124 % | <img src="images/01_Sour/004_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%E5%8F%B3.png" alt="Sour式初音 ウィンク右" width="144"> | <img src="images/02_YYB/017_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%E5%8F%B3.png" alt="YYB式初音 ウィンク右" width="144"> | 未找到 | <img src="images/04_TDA/004_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%E5%8F%B3.png" alt="TDA式初音 ウィンク右" width="144"> |
| 5 | ウィンク２ | 眼部 | 2.898551 % | <img src="images/01_Sour/005_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%EF%BC%92.png" alt="Sour式初音 ウィンク２" width="144"> | <img src="images/02_YYB/018_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%EF%BC%92.png" alt="YYB式初音 ウィンク２" width="144"> | 未找到 | <img src="images/04_TDA/005_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%EF%BC%92.png" alt="TDA式初音 ウィンク２" width="144"> |
| 6 | ｳｨﾝｸ２右 | 眼部 | 2.277433 % | <img src="images/01_Sour/006_%EF%BD%B3%EF%BD%A8%EF%BE%9D%EF%BD%B8%EF%BC%92%E5%8F%B3.png" alt="Sour式初音 ｳｨﾝｸ２右" width="144"> | <img src="images/02_YYB/019_%EF%BD%B3%EF%BD%A8%EF%BE%9D%EF%BD%B8%EF%BC%92%E5%8F%B3.png" alt="YYB式初音 ｳｨﾝｸ２右" width="144"> | 未找到 | <img src="images/04_TDA/006_%EF%BD%B3%EF%BD%A8%EF%BE%9D%EF%BD%B8%EF%BC%92%E5%8F%B3.png" alt="TDA式初音 ｳｨﾝｸ２右" width="144"> |
| 7 | なごみ | 眼部 | 7.660456 % | <img src="images/01_Sour/007_%E3%81%AA%E3%81%94%E3%81%BF.png" alt="Sour式初音 なごみ" width="144"> | <img src="images/02_YYB/023_%E3%81%AA%E3%81%94%E3%81%BF.png" alt="YYB式初音 なごみ" width="144"> | <img src="images/03_Appearance/020_%E3%81%AA%E3%81%94%E3%81%BF.png" alt="Appearance Miku なごみ" width="144"> | <img src="images/04_TDA/007_%E3%81%AA%E3%81%94%E3%81%BF.png" alt="TDA式初音 なごみ" width="144"> |
| 8 | はぅ | 眼部 | 17.18427 % | <img src="images/01_Sour/008_%E3%81%AF%E3%81%85.png" alt="Sour式初音 はぅ" width="144"> | <img src="images/02_YYB/024_%E3%81%AF%E3%81%85.png" alt="YYB式初音 はぅ" width="144"> | <img src="images/03_Appearance/019_%E3%81%AF%E3%81%85.png" alt="Appearance Miku はぅ" width="144"> | <img src="images/04_TDA/008_%E3%81%AF%E3%81%85.png" alt="TDA式初音 はぅ" width="144"> |
| 9 | びっくり | 眼部 | 9.937888 % | <img src="images/01_Sour/011_%E3%81%B3%E3%81%A3%E3%81%8F%E3%82%8A.png" alt="Sour式初音 びっくり" width="144"> | <img src="images/02_YYB/025_%E3%81%B3%E3%81%A3%E3%81%8F%E3%82%8A.png" alt="YYB式初音 びっくり" width="144"> | <img src="images/03_Appearance/021_%E3%81%B3%E3%81%A3%E3%81%8F%E3%82%8A.png" alt="Appearance Miku びっくり" width="144"> | <img src="images/04_TDA/009_%E3%81%B3%E3%81%A3%E3%81%8F%E3%82%8A.png" alt="TDA式初音 びっくり" width="144"> |
| 10 | じと目 | 眼部 | 10.35197 % | <img src="images/01_Sour/012_%E3%81%98%E3%81%A8%E7%9B%AE.png" alt="Sour式初音 じと目" width="144"> | <img src="images/02_YYB/026_%E3%81%98%E3%81%A8%E7%9B%AE.png" alt="YYB式初音 じと目" width="144"> | <img src="images/03_Appearance/022_%E3%81%98%E3%81%A8%E7%9B%AE.png" alt="Appearance Miku じと目" width="144"> | <img src="images/04_TDA/010_%E3%81%98%E3%81%A8%E7%9B%AE.png" alt="TDA式初音 じと目" width="144"> |
| 11 | ｷﾘｯ | 眼部 | 2.484472 % | <img src="images/01_Sour/013_%EF%BD%B7%EF%BE%98%EF%BD%AF.png" alt="Sour式初音 ｷﾘｯ" width="144"> | <img src="images/02_YYB/021_%EF%BD%B7%EF%BE%98%EF%BD%AF.png" alt="YYB式初音 ｷﾘｯ" width="144"> | <img src="images/03_Appearance/023_%EF%BD%B7%EF%BE%98%EF%BD%AF.png" alt="Appearance Miku ｷﾘｯ" width="144"> | <img src="images/04_TDA/011_%EF%BD%B7%EF%BE%98%EF%BD%AF.png" alt="TDA式初音 ｷﾘｯ" width="144"> |
| 12 | はちゅ目 | 眼部 | 0.2070393 % | <img src="images/01_Sour/015_%E3%81%AF%E3%81%A1%E3%82%85%E7%9B%AE.png" alt="Sour式初音 はちゅ目" width="144"> | <img src="images/02_YYB/030_%E3%81%AF%E3%81%A1%E3%82%85%E7%9B%AE.png" alt="YYB式初音 はちゅ目" width="144"> | 未找到 | <img src="images/04_TDA/012_%E3%81%AF%E3%81%A1%E3%82%85%E7%9B%AE.png" alt="TDA式初音 はちゅ目" width="144"> |
| 13 | 星目 | 其他 | 0.4140787 % | <img src="images/01_Sour/021_%E6%98%9F%E7%9B%AE.png" alt="Sour式初音 星目" width="144"> | 未找到 | 未找到 | <img src="images/04_TDA/041_%E6%98%9F%E7%9B%AE.png" alt="TDA式初音 星目" width="144"> |
| 14 | はぁと | 其他 | 0.4140787 % | <img src="images/01_Sour/020_%E3%81%AF%E3%81%81%E3%81%A8.png" alt="Sour式初音 はぁと" width="144"> | 未找到 | 未找到 | <img src="images/04_TDA/042_%E3%81%AF%E3%81%81%E3%81%A8.png" alt="TDA式初音 はぁと" width="144"> |
| 15 | 瞳小 | 其他 | 19.87578 % | <img src="images/01_Sour/026_%E7%9E%B3%E5%B0%8F.png" alt="Sour式初音 瞳小" width="144"> | <img src="images/02_YYB/027_%E7%9E%B3%E5%B0%8F.png" alt="YYB式初音 瞳小" width="144"> | <img src="images/03_Appearance/042_%E7%9E%B3%E5%B0%8F.png" alt="Appearance Miku 瞳小" width="144"> | <img src="images/04_TDA/043_%E7%9E%B3%E5%B0%8F.png" alt="TDA式初音 瞳小" width="144"> |
| 16 | 瞳縦潰れ | 其他 | — | 未找到 | 未找到 | 未找到 | <img src="images/04_TDA/044_%E7%9E%B3%E7%B8%A6%E6%BD%B0%E3%82%8C.png" alt="TDA式初音 瞳縦潰れ" width="144"> |
| 17 | 光下 | 其他 | — | 未找到 | 未找到 | 未找到 | <img src="images/04_TDA/045_%E5%85%89%E4%B8%8B.png" alt="TDA式初音 光下" width="144"> |
| 18 | 恐ろしい子！ | 眼部 | 1.449275 % | <img src="images/01_Sour/025_%E6%81%90%E3%82%8D%E3%81%97%E3%81%84%E5%AD%90%EF%BC%81.png" alt="Sour式初音 恐ろしい子！" width="144"> | 未找到 | 未找到 | <img src="images/04_TDA/046_%E6%81%90%E3%82%8D%E3%81%97%E3%81%84%E5%AD%90%EF%BC%81.png" alt="TDA式初音 恐ろしい子！" width="144"> |
| 19 | ハイライト消 | 其他 | — | 未找到 | 未找到 | 未找到 | 未找到 |
| 20 | 映り込み消 | 其他 | — | 未找到 | 未找到 | 未找到 | 未找到 |
| 21 | 喜び | 眼部 | — | 未找到 | 未找到 | 未找到 | 未找到 |
| 22 | わぉ?! | 其他 | — | 未找到 | 未找到 | 未找到 | 未找到 |
| 23 | なごみω | 其他 | — | 未找到 | 未找到 | 未找到 | 未找到 |
| 24 | 悲しむ | 眼部 | — | 未找到 | 未找到 | 未找到 | 未找到 |
| 25 | 敵意 | 其他 | — | 未找到 | 未找到 | 未找到 | 未找到 |
| 26 | あ | 口部 | 90.89027 % | <img src="images/01_Sour/074_%E3%81%82E.png" alt="Sour式初音 あE" width="144"><br>候选变体：あE | <img src="images/02_YYB/059_x%E3%81%82.png" alt="YYB式初音 xあ" width="144"><br>候选变体：xあ | <img src="images/03_Appearance/001_%E3%81%82.png" alt="Appearance Miku あ" width="144"> | <img src="images/04_TDA/015_%E3%81%82.png" alt="TDA式初音 あ" width="144"> |
| 27 | い | 口部 | 86.74948 % | <img src="images/01_Sour/076_%E3%81%84E.png" alt="Sour式初音 いE" width="144"><br>候选变体：いE | <img src="images/02_YYB/063_x%E3%81%84.png" alt="YYB式初音 xい" width="144"><br>候选变体：xい | <img src="images/03_Appearance/002_%E3%81%84.png" alt="Appearance Miku い" width="144"> | <img src="images/04_TDA/016_%E3%81%84.png" alt="TDA式初音 い" width="144"> |
| 28 | う | 口部 | 81.15942 % | <img src="images/01_Sour/078_%E3%81%86E.png" alt="Sour式初音 うE" width="144"><br>候选变体：うE | <img src="images/02_YYB/068_x%E3%81%86.png" alt="YYB式初音 xう" width="144"><br>候选变体：xう | <img src="images/03_Appearance/003_%E3%81%86.png" alt="Appearance Miku う" width="144"> | <img src="images/04_TDA/017_%E3%81%86.png" alt="TDA式初音 う" width="144"> |
| 29 | え | 口部 | 46.37681 % | <img src="images/01_Sour/080_%E3%81%88E.png" alt="Sour式初音 えE" width="144"><br>候选变体：えE | <img src="images/02_YYB/069_x%E3%81%88.png" alt="YYB式初音 xえ" width="144"><br>候选变体：xえ | <img src="images/03_Appearance/004_%E3%81%88.png" alt="Appearance Miku え" width="144"> | <img src="images/04_TDA/018_%E3%81%88.png" alt="TDA式初音 え" width="144"> |
| 30 | お | 口部 | 87.57764 % | <img src="images/01_Sour/082_%E3%81%8AE.png" alt="Sour式初音 おE" width="144"><br>候选变体：おE | <img src="images/02_YYB/070_x%E3%81%8A.png" alt="YYB式初音 xお" width="144"><br>候选变体：xお | <img src="images/03_Appearance/005_%E3%81%8A.png" alt="Appearance Miku お" width="144"> | <img src="images/04_TDA/019_%E3%81%8A.png" alt="TDA式初音 お" width="144"> |
| 31 | あ２ | 口部 | 0.8281574 % | <img src="images/01_Sour/075_%E3%81%822E.png" alt="Sour式初音 あ2E" width="144"><br>候选变体：あ2E | <img src="images/02_YYB/060_x%E3%81%82%EF%BC%92.png" alt="YYB式初音 xあ２" width="144"><br>候选变体：xあ２ | 未找到 | <img src="images/04_TDA/020_%E3%81%82%EF%BC%92.png" alt="TDA式初音 あ２" width="144"> |
| 32 | ん | 口部 | 4.761905 % | <img src="images/01_Sour/029_%E3%82%93.png" alt="Sour式初音 ん" width="144"> | <img src="images/02_YYB/033_%E3%82%93.png" alt="YYB式初音 ん" width="144"> | 未找到 | <img src="images/04_TDA/021_%E3%82%93.png" alt="TDA式初音 ん" width="144"> |
| 33 | ▲ | 口部 | 2.484472 % | <img src="images/01_Sour/083_%E2%96%B2E.png" alt="Sour式初音 ▲E" width="144"><br>候选变体：▲E | 未找到 | <img src="images/03_Appearance/006_%E2%96%B2.png" alt="Appearance Miku ▲" width="144"> | <img src="images/04_TDA/022_%E2%96%B2.png" alt="TDA式初音 ▲" width="144"> |
| 34 | ∧ | 口部 | 3.933748 % | <img src="images/01_Sour/030_%E2%88%A7.png" alt="Sour式初音 ∧" width="144"> | <img src="images/02_YYB/034_%E2%88%A7.png" alt="YYB式初音 ∧" width="144"> | <img src="images/03_Appearance/007_%E2%88%A7.png" alt="Appearance Miku ∧" width="144"> | <img src="images/04_TDA/023_%E2%88%A7.png" alt="TDA式初音 ∧" width="144"> |
| 35 | □ | 口部 | 0.4140787 % | <img src="images/01_Sour/084_%E2%96%A1E.png" alt="Sour式初音 □E" width="144"><br>候选变体：□E | <img src="images/02_YYB/035_%E2%96%A1.png" alt="YYB式初音 □" width="144"> | 未找到 | <img src="images/04_TDA/024_%E2%96%A1.png" alt="TDA式初音 □" width="144"> |
| 36 | ワ | 口部 | 7.453416 % | <img src="images/01_Sour/085_%E3%83%AFE.png" alt="Sour式初音 ワE" width="144"><br>候选变体：ワE | 未找到 | <img src="images/03_Appearance/010_%E3%83%AF.png" alt="Appearance Miku ワ" width="144"> | <img src="images/04_TDA/025_%E3%83%AF.png" alt="TDA式初音 ワ" width="144"> |
| 37 | ω | 口部 | 3.519669 % | <img src="images/01_Sour/087_%CF%89E.png" alt="Sour式初音 ωE" width="144"><br>候选变体：ωE | <img src="images/02_YYB/036_%CF%89.png" alt="YYB式初音 ω" width="144"> | <img src="images/03_Appearance/008_%CF%89.png" alt="Appearance Miku ω" width="144"> | <img src="images/04_TDA/026_%CF%89.png" alt="TDA式初音 ω" width="144"> |
| 38 | ω□ | 口部 | — | <img src="images/01_Sour/088_%CF%89%E2%96%A1E.png" alt="Sour式初音 ω□E" width="144"><br>候选变体：ω□E | <img src="images/02_YYB/037_%CF%89%E2%96%A1.png" alt="YYB式初音 ω□" width="144"> | <img src="images/03_Appearance/009_%CF%89%E2%96%A1.png" alt="Appearance Miku ω□" width="144"> | <img src="images/04_TDA/027_%CF%89%E2%96%A1.png" alt="TDA式初音 ω□" width="144"> |
| 39 | にやり | 口部 | 22.77433 % | <img src="images/01_Sour/089_%E3%81%AB%E3%82%84%E3%82%8AE.png" alt="Sour式初音 にやりE" width="144"><br>候选变体：にやりE | <img src="images/02_YYB/038_%E3%81%AB%E3%82%84%E3%82%8A.png" alt="YYB式初音 にやり" width="144"> | <img src="images/03_Appearance/015_%E3%81%AB%E3%82%84%E3%82%8A.png" alt="Appearance Miku にやり" width="144"> | <img src="images/04_TDA/028_%E3%81%AB%E3%82%84%E3%82%8A.png" alt="TDA式初音 にやり" width="144"> |
| 40 | にやり２ | 口部 | 1.863354 % | 未找到 | 未找到 | 未找到 | <img src="images/04_TDA/029_%E3%81%AB%E3%82%84%E3%82%8A%EF%BC%92.png" alt="TDA式初音 にやり２" width="144"> |
| 41 | にっこり | 口部 | 4.968944 % | <img src="images/01_Sour/090_%E3%81%AB%E3%81%A3%E3%81%93%E3%82%8AE.png" alt="Sour式初音 にっこりE" width="144"><br>候选变体：にっこりE | 未找到 | 未找到 | <img src="images/04_TDA/030_%E3%81%AB%E3%81%A3%E3%81%93%E3%82%8A.png" alt="TDA式初音 にっこり" width="144"> |
| 42 | ぺろっ | 口部 | 0.2070393 % | 未找到 | <img src="images/02_YYB/039_%E3%81%BA%E3%82%8D%E3%81%A3.png" alt="YYB式初音 ぺろっ" width="144"> | 未找到 | <img src="images/04_TDA/031_%E3%81%BA%E3%82%8D%E3%81%A3.png" alt="TDA式初音 ぺろっ" width="144"> |
| 43 | てへぺろ | 口部 | — | 未找到 | 未找到 | 未找到 | <img src="images/04_TDA/032_%E3%81%A6%E3%81%B8%E3%81%BA%E3%82%8D.png" alt="TDA式初音 てへぺろ" width="144"> |
| 44 | てへぺろ２ | 口部 | — | 未找到 | 未找到 | 未找到 | <img src="images/04_TDA/033_%E3%81%A6%E3%81%B8%E3%81%BA%E3%82%8D%EF%BC%92.png" alt="TDA式初音 てへぺろ２" width="144"> |
| 45 | 口角上げ | 口部 | 3.312629 % | <img src="images/01_Sour/032_%E5%8F%A3%E8%A7%92%E4%B8%8A%E3%81%92.png" alt="Sour式初音 口角上げ" width="144"> | <img src="images/02_YYB/041_%E5%8F%A3%E8%A7%92%E4%B8%8A%E3%81%92.png" alt="YYB式初音 口角上げ" width="144"> | 未找到 | <img src="images/04_TDA/034_%E5%8F%A3%E8%A7%92%E4%B8%8A%E3%81%92.png" alt="TDA式初音 口角上げ" width="144"> |
| 46 | 口角下げ | 口部 | 1.863354 % | <img src="images/01_Sour/033_%E5%8F%A3%E8%A7%92%E4%B8%8B%E3%81%92.png" alt="Sour式初音 口角下げ" width="144"> | <img src="images/02_YYB/044_%E5%8F%A3%E8%A7%92%E4%B8%8B%E3%81%92.png" alt="YYB式初音 口角下げ" width="144"> | 未找到 | <img src="images/04_TDA/035_%E5%8F%A3%E8%A7%92%E4%B8%8B%E3%81%92.png" alt="TDA式初音 口角下げ" width="144"> |
| 47 | 口横広げ | 口部 | 1.863354 % | <img src="images/01_Sour/034_%E5%8F%A3%E6%A8%AA%E5%BA%83%E3%81%92.png" alt="Sour式初音 口横広げ" width="144"> | <img src="images/02_YYB/047_%E5%8F%A3%E6%A8%AA%E5%BA%83%E3%81%92.png" alt="YYB式初音 口横広げ" width="144"> | 未找到 | <img src="images/04_TDA/036_%E5%8F%A3%E6%A8%AA%E5%BA%83%E3%81%92.png" alt="TDA式初音 口横広げ" width="144"> |
| 48 | 歯無し上 | 口部 | — | 未找到 | 未找到 | 未找到 | <img src="images/04_TDA/037_%E6%AD%AF%E7%84%A1%E3%81%97%E4%B8%8A.png" alt="TDA式初音 歯無し上" width="144"><br>头部画面变化很小，待核对<br>组合辅助：あ=1 + 歯無し上=1<br><img src="images/04_TDA/context_%E6%AD%AF%E7%84%A1%E3%81%97%E4%B8%8A%2B%E3%81%82.png" alt="歯無し上 组合辅助" width="144"> |
| 49 | 歯無し下 | 口部 | — | 未找到 | 未找到 | 未找到 | <img src="images/04_TDA/038_%E6%AD%AF%E7%84%A1%E3%81%97%E4%B8%8B.png" alt="TDA式初音 歯無し下" width="144"><br>头部画面变化很小，待核对<br>组合辅助：あ=1 + 歯無し下=1<br><img src="images/04_TDA/context_%E6%AD%AF%E7%84%A1%E3%81%97%E4%B8%8B%2B%E3%81%82.png" alt="歯無し下 组合辅助" width="144"><br>组合中仍无明显可见变化，待核对 |
| 50 | 真面目 | 其他 | 23.18841 % | <img src="images/01_Sour/036_%E7%9C%9F%E9%9D%A2%E7%9B%AE.png" alt="Sour式初音 真面目" width="144"> | <img src="images/02_YYB/001_%E7%9C%9F%E9%9D%A2%E7%9B%AE.png" alt="YYB式初音 真面目" width="144"> | <img src="images/03_Appearance/029_%E7%9C%9F%E9%9D%A2%E7%9B%AE.png" alt="Appearance Miku 真面目" width="144"> | <img src="images/04_TDA/049_%E7%9C%9F%E9%9D%A2%E7%9B%AE.png" alt="TDA式初音 真面目" width="144"> |
| 51 | 困る | 其他 | 49.06832 % | <img src="images/01_Sour/039_%E5%9B%B0%E3%82%8B.png" alt="Sour式初音 困る" width="144"> | <img src="images/02_YYB/002_%E5%9B%B0%E3%82%8B.png" alt="YYB式初音 困る" width="144"> | <img src="images/03_Appearance/030_%E5%9B%B0%E3%82%8B.png" alt="Appearance Miku 困る" width="144"> | <img src="images/04_TDA/050_%E5%9B%B0%E3%82%8B.png" alt="TDA式初音 困る" width="144"> |
| 52 | にこり | 其他 | 17.59834 % | <img src="images/01_Sour/042_%E3%81%AB%E3%81%93%E3%82%8A.png" alt="Sour式初音 にこり" width="144"> | <img src="images/02_YYB/004_%E3%81%AB%E3%81%93%E3%82%8A.png" alt="YYB式初音 にこり" width="144"> | <img src="images/03_Appearance/031_%E3%81%AB%E3%81%93%E3%82%8A.png" alt="Appearance Miku にこり" width="144"> | <img src="images/04_TDA/051_%E3%81%AB%E3%81%93%E3%82%8A.png" alt="TDA式初音 にこり" width="144"> |
| 53 | 怒り | 其他 | 28.36439 % | <img src="images/01_Sour/045_%E6%80%92%E3%82%8A.png" alt="Sour式初音 怒り" width="144"> | <img src="images/02_YYB/005_%E6%80%92%E3%82%8A.png" alt="YYB式初音 怒り" width="144"> | <img src="images/03_Appearance/032_%E6%80%92%E3%82%8A.png" alt="Appearance Miku 怒り" width="144"> | <img src="images/04_TDA/052_%E6%80%92%E3%82%8A.png" alt="TDA式初音 怒り" width="144"> |
| 54 | 上 | 其他 | 25.67288 % | <img src="images/01_Sour/051_%E4%B8%8A.png" alt="Sour式初音 上" width="144"> | <img src="images/02_YYB/007_%E4%B8%8A.png" alt="YYB式初音 上" width="144"> | <img src="images/03_Appearance/037_%E4%B8%8A.png" alt="Appearance Miku 上" width="144"> | <img src="images/04_TDA/053_%E4%B8%8A.png" alt="TDA式初音 上" width="144"> |
| 55 | 下 | 其他 | 40.37267 % | <img src="images/01_Sour/054_%E4%B8%8B.png" alt="Sour式初音 下" width="144"> | <img src="images/02_YYB/010_%E4%B8%8B.png" alt="YYB式初音 下" width="144"> | <img src="images/03_Appearance/038_%E4%B8%8B.png" alt="Appearance Miku 下" width="144"> | <img src="images/04_TDA/054_%E4%B8%8B.png" alt="TDA式初音 下" width="144"> |

## 模型独有项与全部渲染

以下页面列出各模型**全部实际形态键**，包括预设外项目，方便下一轮验证预设是否足够。

- [Sour式初音：94 项全部图片](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/01_Sour.md)；其中 54 项未用于主表。
- [YYB式初音：73 项全部图片](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/02_YYB.md)；其中 38 项未用于主表。
- [Appearance Miku：45 项全部图片](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/03_Appearance.md)；其中 20 项未用于主表。
- [TDA式初音：63 项全部图片](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/04_TDA.md)；其中 15 项未用于主表。

## 渲染核验

- 已检查 287 张 PNG：文件可解码、尺寸全部为 512 × 512、图像不是全透明空图。
- `render_validation.json` 保留逐图 SHA-256、相对基准的像素差异和低变化项目；组合辅助图与其基础键图比较。
- 有 20 个项目在头部画面中变化很小，明细中已标注；这可能是换装/附件键、隐藏部件、微小调整或需进一步检查的项目。
- 图像差异只用于排查空白/重复结果，不代替表情语义和模型制作正确性的人工判断。
- 当前工程存在一处原有骨约束依赖循环，Blender 在载入时报告；渲染任务已完成，原工程未作修复。

## lil 统计附录

- [lilxyzw 完整统计表、精选列表、样本与统计口径](%E9%99%84%E5%BD%95/lil_MMD%E8%A1%A8%E6%83%85%E7%BB%9F%E8%AE%A1.md)
- 原始 Gist：<https://gist.github.com/lilxyzw/80608d9b16bf3458c61dec6b090805c5>。
- 原始 TXT、Gist JSON 快照和本次 HoTools 预设 CSV 都在 `附录` 中。

## 可复现文件

- `scripts/render_expressions.py`：Blender 批量渲染脚本。
- `scripts/build_reference.py`：生成表格、明细与图像核验。
- `scene_inventory.json`：集合、骨架、形态键、材质、贴图清单。
- `0*_renders.json`：每个模型的镜头、实际键名和图片路径。
- `预设与模型对应.csv`：按预设原始顺序排列的 55 × 4 项名称映射。
- `render_validation.json`：完整图像核验。
- `render.log`：Blender 渲染日志。
