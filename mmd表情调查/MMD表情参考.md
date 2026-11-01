# MMD 表情参考

- 制作日期：2026-11-01（Asia/Shanghai）。
- 源工程：`C:\Users\hhh12\Desktop\mmd表情研究.blend`；原始工程未覆盖保存。
- 主表以 lilxyzw 完整统计中的 **245 个原始表情名称**为准，按动作使用率从高到低排列；同频保持源文件顺序。
- HoTools 的 **55 条 MMD TEMPLATE** 仅作为预设对照列，未收录的统计名称也全部保留。
- 本次输出：**275 张单项形态键图 + 4 张基准图 + 8 张组合辅助图**，全部为 **512 × 512 PNG**。
- 四个模型均以各自骨架的 **“頭”骨**定位，结合眼骨朝向与脸部材质包围盒确定正面正交机位。
- 每次只激活一个实际形态键（值 1.0），其余归零。同一模型的机位、灯光和取景固定；128 渲染采样，透明背景。
- 牙齿和特殊眼的组合辅助图另行启用一个基础键，**两个键均为 1.0**；图片明确标注组合，不与单项图混淆。
- 材质按工程磁盘保存状态原样使用。检查到的主要连接为 `MMDShaderDev` 等节点组，未检测到名含 `HoToon` 的节点；没有为此替换或重建材质。
- `Basis` 和 `mmd_sdef_c / mmd_sdef_r0 / mmd_sdef_r1` 是基准/辅助数据，不当作表情渲染。
- 模型原有的换装、附件、局部调节键同样保留独立渲染，放入模型明细；头部取景下可能没有明显差异。
- 此版本用于完整统计与实际模型的视觉对照，暂不据此宣称预设完整，也不修改插件中的预设。

## 阅读方式

- 表内使用标准 Markdown 缩略图链接；点击缩略图可打开 512 × 512 原图。缩略图单独保存在 `images/thumbnails/`。
- **完全同名**：主表默认直接展示图片。
- **全半角兼容**：仅统一 Unicode 全半角；图片旁注明原始键名。
- **候选变体**：仅明确列出 `x` 前缀或 `E` 后缀的作者变体，供视觉研究；不计入完全同名覆盖，不据名称断言等价。
- **未找到**：该模型没有对应键，也没有采用上述候选命名。不会生成一张基准图冒充该表情。
- **HoTools 预设**：仅当该统计原名与现有 TEMPLATE 完全同名时标记“是”；不据此合并统计中的名称变体。
- lil 的原始名称、全半角、大小写及频率精度全部保留；即使四个模型都未找到图片，该行也会保留。
- lil 使用率是 **483 个动作中的使用率**，不是模型拥有率；下方汇总为统计名称的匹配情况，不直接等同功能覆盖率。

## 模型与统计名称对应

| 模型集合 | 骨架 | 实际形态键图 | 完全同名 | 全半角兼容 | 候选变体 | 未找到 | 全部原名与图片 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Sour式初音 | Black_arm | 94 | 40 | 2 | 15 | 188 | [模型明细](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/01_Sour.md) |
| YYB式初音 | YYB Hatsune Miku default 1.0ver_arm | 73 | 30 | 2 | 9 | 204 | [模型明细](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/02_YYB.md) |
| Appearance Miku | Appearance Miku_arm | 45 | 31 | 0 | 0 | 214 | [模型明细](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/03_Appearance.md) |
| TDA式初音 | Tda式初音ミクV4X Ver1.00_arm | 63 | 45 | 3 | 0 | 197 | [模型明细](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/04_TDA.md) |

## 无表情基准

| Sour式初音 | YYB式初音 | Appearance Miku | TDA式初音 |
| --- | --- | --- | --- |
| [![Sour式初音 基准](images/thumbnails/220/4fa774b1b9431cc8.png)](images/01_Sour/000_%E5%9F%BA%E5%87%86.png) | [![YYB式初音 基准](images/thumbnails/220/f41e287329212190.png)](images/02_YYB/000_%E5%9F%BA%E5%87%86.png) | [![Appearance Miku 基准](images/thumbnails/220/f285f35c35a37528.png)](images/03_Appearance/000_%E5%9F%BA%E5%87%86.png) | [![TDA式初音 基准](images/thumbnails/220/ab54701186cb49e1.png)](images/04_TDA/000_%E5%9F%BA%E5%87%86.png) |

## lil 全部表情参考表（245 项，使用率降序）

| 排名 | lil 统计原名 | 动作使用率 | HoTools 预设 | Sour式初音 | YYB式初音 | Appearance Miku | TDA式初音 |
| ---: | --- | ---: | --- | --- | --- | --- | --- |
| 1 | あ | 90.89027 % | 是 | [![Sour式初音 あE](images/thumbnails/144/0dd5be5413c506ae.png)](images/01_Sour/074_%E3%81%82E.png) 候选变体：あE | [![YYB式初音 xあ](images/thumbnails/144/055275522b238590.png)](images/02_YYB/059_x%E3%81%82.png) 候选变体：xあ | [![Appearance Miku あ](images/thumbnails/144/a277207b95f0a7cc.png)](images/03_Appearance/001_%E3%81%82.png) | [![TDA式初音 あ](images/thumbnails/144/0d15b92f894b2ca5.png)](images/04_TDA/015_%E3%81%82.png) |
| 2 | まばたき | 87.57764 % | 是 | [![Sour式初音 まばたき](images/thumbnails/144/bd0909963bf114cc.png)](images/01_Sour/001_%E3%81%BE%E3%81%B0%E3%81%9F%E3%81%8D.png) | [![YYB式初音 まばたき](images/thumbnails/144/f10af2b8cfedfc53.png)](images/02_YYB/014_%E3%81%BE%E3%81%B0%E3%81%9F%E3%81%8D.png) | [![Appearance Miku まばたき](images/thumbnails/144/cf98c7b61ed52efa.png)](images/03_Appearance/016_%E3%81%BE%E3%81%B0%E3%81%9F%E3%81%8D.png) | [![TDA式初音 まばたき](images/thumbnails/144/83c8d809907cf0c7.png)](images/04_TDA/001_%E3%81%BE%E3%81%B0%E3%81%9F%E3%81%8D.png) |
| 3 | お | 87.57764 % | 是 | [![Sour式初音 おE](images/thumbnails/144/a0754b3c1b038bc8.png)](images/01_Sour/082_%E3%81%8AE.png) 候选变体：おE | [![YYB式初音 xお](images/thumbnails/144/4a8e7e502d5f735b.png)](images/02_YYB/070_x%E3%81%8A.png) 候选变体：xお | [![Appearance Miku お](images/thumbnails/144/1acc8fd12f4368b7.png)](images/03_Appearance/005_%E3%81%8A.png) | [![TDA式初音 お](images/thumbnails/144/7a6fdd81e216750e.png)](images/04_TDA/019_%E3%81%8A.png) |
| 4 | い | 86.74948 % | 是 | [![Sour式初音 いE](images/thumbnails/144/4076d54d691adfe1.png)](images/01_Sour/076_%E3%81%84E.png) 候选变体：いE | [![YYB式初音 xい](images/thumbnails/144/5773a1b4fabc0c1f.png)](images/02_YYB/063_x%E3%81%84.png) 候选变体：xい | [![Appearance Miku い](images/thumbnails/144/4ca49cb577d0dd40.png)](images/03_Appearance/002_%E3%81%84.png) | [![TDA式初音 い](images/thumbnails/144/0ab22be2c748374b.png)](images/04_TDA/016_%E3%81%84.png) |
| 5 | う | 81.15942 % | 是 | [![Sour式初音 うE](images/thumbnails/144/54001a04fcf716bb.png)](images/01_Sour/078_%E3%81%86E.png) 候选变体：うE | [![YYB式初音 xう](images/thumbnails/144/31314c3b0b8ed677.png)](images/02_YYB/068_x%E3%81%86.png) 候选变体：xう | [![Appearance Miku う](images/thumbnails/144/859c26a7d0561c40.png)](images/03_Appearance/003_%E3%81%86.png) | [![TDA式初音 う](images/thumbnails/144/1a599610c2582e1a.png)](images/04_TDA/017_%E3%81%86.png) |
| 6 | 笑い | 68.73706 % | 是 | [![Sour式初音 笑い](images/thumbnails/144/c153293986dcb535.png)](images/01_Sour/002_%E7%AC%91%E3%81%84.png) | [![YYB式初音 笑い](images/thumbnails/144/8faa1eb8f792d985.png)](images/02_YYB/015_%E7%AC%91%E3%81%84.png) | [![Appearance Miku 笑い](images/thumbnails/144/fd8a85c9e684a13c.png)](images/03_Appearance/017_%E7%AC%91%E3%81%84.png) | [![TDA式初音 笑い](images/thumbnails/144/0faa32db880525ee.png)](images/04_TDA/002_%E7%AC%91%E3%81%84.png) |
| 7 | 困る | 49.06832 % | 是 | [![Sour式初音 困る](images/thumbnails/144/d3e8532badc796af.png)](images/01_Sour/039_%E5%9B%B0%E3%82%8B.png) | [![YYB式初音 困る](images/thumbnails/144/b709d7d28c4f19a6.png)](images/02_YYB/002_%E5%9B%B0%E3%82%8B.png) | [![Appearance Miku 困る](images/thumbnails/144/27b32d894daf799b.png)](images/03_Appearance/030_%E5%9B%B0%E3%82%8B.png) | [![TDA式初音 困る](images/thumbnails/144/ded184a8c42db005.png)](images/04_TDA/050_%E5%9B%B0%E3%82%8B.png) |
| 8 | え | 46.37681 % | 是 | [![Sour式初音 えE](images/thumbnails/144/aa456d5e54083d42.png)](images/01_Sour/080_%E3%81%88E.png) 候选变体：えE | [![YYB式初音 xえ](images/thumbnails/144/55d8f31736875a3f.png)](images/02_YYB/069_x%E3%81%88.png) 候选变体：xえ | [![Appearance Miku え](images/thumbnails/144/1ec9ea37e1ba9fcc.png)](images/03_Appearance/004_%E3%81%88.png) | [![TDA式初音 え](images/thumbnails/144/a8ecaa5cfb35d906.png)](images/04_TDA/018_%E3%81%88.png) |
| 9 | 下 | 40.37267 % | 是 | [![Sour式初音 下](images/thumbnails/144/a19d8f62b4dcd725.png)](images/01_Sour/054_%E4%B8%8B.png) | [![YYB式初音 下](images/thumbnails/144/f6c92251a378d4b6.png)](images/02_YYB/010_%E4%B8%8B.png) | [![Appearance Miku 下](images/thumbnails/144/69179ab977e41dbc.png)](images/03_Appearance/038_%E4%B8%8B.png) | [![TDA式初音 下](images/thumbnails/144/7ff94abe2f817534.png)](images/04_TDA/054_%E4%B8%8B.png) |
| 10 | 怒り | 28.36439 % | 是 | [![Sour式初音 怒り](images/thumbnails/144/da196af9b385b873.png)](images/01_Sour/045_%E6%80%92%E3%82%8A.png) | [![YYB式初音 怒り](images/thumbnails/144/0a2b7c9e63a4cec1.png)](images/02_YYB/005_%E6%80%92%E3%82%8A.png) | [![Appearance Miku 怒り](images/thumbnails/144/1299ff38af801295.png)](images/03_Appearance/032_%E6%80%92%E3%82%8A.png) | [![TDA式初音 怒り](images/thumbnails/144/0f2ddf5a8188b376.png)](images/04_TDA/052_%E6%80%92%E3%82%8A.png) |
| 11 | ウィンク | 27.12215 % | 是 | [![Sour式初音 ウィンク](images/thumbnails/144/3a39321c1f2fb58a.png)](images/01_Sour/003_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF.png) | [![YYB式初音 ウィンク](images/thumbnails/144/cffc86691b7912de.png)](images/02_YYB/016_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF.png) | 未找到 | [![TDA式初音 ウィンク](images/thumbnails/144/945ba8b2caff6439.png)](images/04_TDA/003_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF.png) |
| 12 | 上 | 25.67288 % | 是 | [![Sour式初音 上](images/thumbnails/144/b0df5e063b0d7dc0.png)](images/01_Sour/051_%E4%B8%8A.png) | [![YYB式初音 上](images/thumbnails/144/07465f0e7d6e71d8.png)](images/02_YYB/007_%E4%B8%8A.png) | [![Appearance Miku 上](images/thumbnails/144/17369ab9f761069e.png)](images/03_Appearance/037_%E4%B8%8A.png) | [![TDA式初音 上](images/thumbnails/144/435c1afe3c6a2f2a.png)](images/04_TDA/053_%E4%B8%8A.png) |
| 13 | 真面目 | 23.18841 % | 是 | [![Sour式初音 真面目](images/thumbnails/144/a17f7daa70b6eed5.png)](images/01_Sour/036_%E7%9C%9F%E9%9D%A2%E7%9B%AE.png) | [![YYB式初音 真面目](images/thumbnails/144/f5ee57750574f9ab.png)](images/02_YYB/001_%E7%9C%9F%E9%9D%A2%E7%9B%AE.png) | [![Appearance Miku 真面目](images/thumbnails/144/b2d91f8b3a3b3d3c.png)](images/03_Appearance/029_%E7%9C%9F%E9%9D%A2%E7%9B%AE.png) | [![TDA式初音 真面目](images/thumbnails/144/11297a8703ead1e9.png)](images/04_TDA/049_%E7%9C%9F%E9%9D%A2%E7%9B%AE.png) |
| 14 | にやり | 22.77433 % | 是 | [![Sour式初音 にやりE](images/thumbnails/144/9c5ecd2507cbe00f.png)](images/01_Sour/089_%E3%81%AB%E3%82%84%E3%82%8AE.png) 候选变体：にやりE | [![YYB式初音 にやり](images/thumbnails/144/b854ee5fff04871f.png)](images/02_YYB/038_%E3%81%AB%E3%82%84%E3%82%8A.png) | [![Appearance Miku にやり](images/thumbnails/144/81b76f105d9e858f.png)](images/03_Appearance/015_%E3%81%AB%E3%82%84%E3%82%8A.png) | [![TDA式初音 にやり](images/thumbnails/144/989535e0ad3bbb89.png)](images/04_TDA/028_%E3%81%AB%E3%82%84%E3%82%8A.png) |
| 15 | 瞳小 | 19.87578 % | 是 | [![Sour式初音 瞳小](images/thumbnails/144/72729cb6092a4b82.png)](images/01_Sour/026_%E7%9E%B3%E5%B0%8F.png) | [![YYB式初音 瞳小](images/thumbnails/144/5cc2ab1af34abdfa.png)](images/02_YYB/027_%E7%9E%B3%E5%B0%8F.png) | [![Appearance Miku 瞳小](images/thumbnails/144/95e2bd23a0bcd337.png)](images/03_Appearance/042_%E7%9E%B3%E5%B0%8F.png) | [![TDA式初音 瞳小](images/thumbnails/144/e11351fa335cad78.png)](images/04_TDA/043_%E7%9E%B3%E5%B0%8F.png) |
| 16 | にこり | 17.59834 % | 是 | [![Sour式初音 にこり](images/thumbnails/144/352d1d7757c44d23.png)](images/01_Sour/042_%E3%81%AB%E3%81%93%E3%82%8A.png) | [![YYB式初音 にこり](images/thumbnails/144/c1913f84255b936b.png)](images/02_YYB/004_%E3%81%AB%E3%81%93%E3%82%8A.png) | [![Appearance Miku にこり](images/thumbnails/144/c9c250c4e8adb748.png)](images/03_Appearance/031_%E3%81%AB%E3%81%93%E3%82%8A.png) | [![TDA式初音 にこり](images/thumbnails/144/af148edb6cd0b613.png)](images/04_TDA/051_%E3%81%AB%E3%81%93%E3%82%8A.png) |
| 17 | はぅ | 17.18427 % | 是 | [![Sour式初音 はぅ](images/thumbnails/144/cc2c2d14cd6a534a.png)](images/01_Sour/008_%E3%81%AF%E3%81%85.png) | [![YYB式初音 はぅ](images/thumbnails/144/fe045b865e13fbaa.png)](images/02_YYB/024_%E3%81%AF%E3%81%85.png) | [![Appearance Miku はぅ](images/thumbnails/144/e50c638efb36b8c0.png)](images/03_Appearance/019_%E3%81%AF%E3%81%85.png) | [![TDA式初音 はぅ](images/thumbnails/144/d858bfe2d1549b17.png)](images/04_TDA/008_%E3%81%AF%E3%81%85.png) |
| 18 | ウィンク右 | 11.80124 % | 是 | [![Sour式初音 ウィンク右](images/thumbnails/144/229d8bf93b293da1.png)](images/01_Sour/004_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%E5%8F%B3.png) | [![YYB式初音 ウィンク右](images/thumbnails/144/5e7e0ed9c9fc5c09.png)](images/02_YYB/017_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%E5%8F%B3.png) | 未找到 | [![TDA式初音 ウィンク右](images/thumbnails/144/92f00d62af8cc4ba.png)](images/04_TDA/004_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%E5%8F%B3.png) |
| 19 | じと目 | 10.35197 % | 是 | [![Sour式初音 じと目](images/thumbnails/144/66ca873b7b362a42.png)](images/01_Sour/012_%E3%81%98%E3%81%A8%E7%9B%AE.png) | [![YYB式初音 じと目](images/thumbnails/144/7512fda33b0f012e.png)](images/02_YYB/026_%E3%81%98%E3%81%A8%E7%9B%AE.png) | [![Appearance Miku じと目](images/thumbnails/144/88f25f00b9141054.png)](images/03_Appearance/022_%E3%81%98%E3%81%A8%E7%9B%AE.png) | [![TDA式初音 じと目](images/thumbnails/144/c6c52518a4ae3701.png)](images/04_TDA/010_%E3%81%98%E3%81%A8%E7%9B%AE.png) |
| 20 | びっくり | 9.937888 % | 是 | [![Sour式初音 びっくり](images/thumbnails/144/e47a0c6bb7f8224b.png)](images/01_Sour/011_%E3%81%B3%E3%81%A3%E3%81%8F%E3%82%8A.png) | [![YYB式初音 びっくり](images/thumbnails/144/7dac1e480a1e89c6.png)](images/02_YYB/025_%E3%81%B3%E3%81%A3%E3%81%8F%E3%82%8A.png) | [![Appearance Miku びっくり](images/thumbnails/144/00bdc1f45b6b3cd9.png)](images/03_Appearance/021_%E3%81%B3%E3%81%A3%E3%81%8F%E3%82%8A.png) | [![TDA式初音 びっくり](images/thumbnails/144/e33c744c6691a3e2.png)](images/04_TDA/009_%E3%81%B3%E3%81%A3%E3%81%8F%E3%82%8A.png) |
| 21 | なごみ | 7.660456 % | 是 | [![Sour式初音 なごみ](images/thumbnails/144/85dad5b4ee365cf7.png)](images/01_Sour/007_%E3%81%AA%E3%81%94%E3%81%BF.png) | [![YYB式初音 なごみ](images/thumbnails/144/51f1e6504d7d8af4.png)](images/02_YYB/023_%E3%81%AA%E3%81%94%E3%81%BF.png) | [![Appearance Miku なごみ](images/thumbnails/144/54b064544b292f89.png)](images/03_Appearance/020_%E3%81%AA%E3%81%94%E3%81%BF.png) | [![TDA式初音 なごみ](images/thumbnails/144/43b966eaede3bda9.png)](images/04_TDA/007_%E3%81%AA%E3%81%94%E3%81%BF.png) |
| 22 | ワ | 7.453416 % | 是 | [![Sour式初音 ワE](images/thumbnails/144/64c8100e14a202fe.png)](images/01_Sour/085_%E3%83%AFE.png) 候选变体：ワE | 未找到 | [![Appearance Miku ワ](images/thumbnails/144/de7d5aa26d231b3c.png)](images/03_Appearance/010_%E3%83%AF.png) | [![TDA式初音 ワ](images/thumbnails/144/158d4922000d1be1.png)](images/04_TDA/025_%E3%83%AF.png) |
| 23 | にっこり | 4.968944 % | 是 | [![Sour式初音 にっこりE](images/thumbnails/144/f2141485b1f0d6bf.png)](images/01_Sour/090_%E3%81%AB%E3%81%A3%E3%81%93%E3%82%8AE.png) 候选变体：にっこりE | 未找到 | 未找到 | [![TDA式初音 にっこり](images/thumbnails/144/09f4bf128bebad65.png)](images/04_TDA/030_%E3%81%AB%E3%81%A3%E3%81%93%E3%82%8A.png) |
| 24 | ん | 4.761905 % | 是 | [![Sour式初音 ん](images/thumbnails/144/6a0aca080426a20a.png)](images/01_Sour/029_%E3%82%93.png) | [![YYB式初音 ん](images/thumbnails/144/499cc21ecef67b39.png)](images/02_YYB/033_%E3%82%93.png) | 未找到 | [![TDA式初音 ん](images/thumbnails/144/b770a339f3cf6b07.png)](images/04_TDA/021_%E3%82%93.png) |
| 25 | 照れ | 4.347826 % | 否 | [![Sour式初音 照れ](images/thumbnails/144/e9ecb06ad676f279.png)](images/01_Sour/060_%E7%85%A7%E3%82%8C.png) | 未找到 | 未找到 | [![TDA式初音 照れ](images/thumbnails/144/6d32544ee28eb5bc.png)](images/04_TDA/047_%E7%85%A7%E3%82%8C.png) |
| 26 | ∧ | 3.933748 % | 是 | [![Sour式初音 ∧](images/thumbnails/144/9a2231336b6de034.png)](images/01_Sour/030_%E2%88%A7.png) | [![YYB式初音 ∧](images/thumbnails/144/4a25928c698d1bd9.png)](images/02_YYB/034_%E2%88%A7.png) | [![Appearance Miku ∧](images/thumbnails/144/63b4baed8586527f.png)](images/03_Appearance/007_%E2%88%A7.png) | [![TDA式初音 ∧](images/thumbnails/144/eb4fa0b3100519a4.png)](images/04_TDA/023_%E2%88%A7.png) |
| 27 | ω | 3.519669 % | 是 | [![Sour式初音 ωE](images/thumbnails/144/6d0b0a4342b4c1d8.png)](images/01_Sour/087_%CF%89E.png) 候选变体：ωE | [![YYB式初音 ω](images/thumbnails/144/59223633db172405.png)](images/02_YYB/036_%CF%89.png) | [![Appearance Miku ω](images/thumbnails/144/6fc3dbb4dcd7c66c.png)](images/03_Appearance/008_%CF%89.png) | [![TDA式初音 ω](images/thumbnails/144/8b87ca222e04fe80.png)](images/04_TDA/026_%CF%89.png) |
| 28 | 口角上げ | 3.312629 % | 是 | [![Sour式初音 口角上げ](images/thumbnails/144/1a03e1ec464aa585.png)](images/01_Sour/032_%E5%8F%A3%E8%A7%92%E4%B8%8A%E3%81%92.png) | [![YYB式初音 口角上げ](images/thumbnails/144/61b3e79dc2ede22c.png)](images/02_YYB/041_%E5%8F%A3%E8%A7%92%E4%B8%8A%E3%81%92.png) | 未找到 | [![TDA式初音 口角上げ](images/thumbnails/144/0c4f2eda126a87a1.png)](images/04_TDA/034_%E5%8F%A3%E8%A7%92%E4%B8%8A%E3%81%92.png) |
| 29 | ウィンク２ | 2.898551 % | 是 | [![Sour式初音 ウィンク２](images/thumbnails/144/6d4681ca545e0244.png)](images/01_Sour/005_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%EF%BC%92.png) | [![YYB式初音 ウィンク２](images/thumbnails/144/bcb5ad2e5aca9be8.png)](images/02_YYB/018_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%EF%BC%92.png) | 未找到 | [![TDA式初音 ウィンク２](images/thumbnails/144/11331d9f4169d49f.png)](images/04_TDA/005_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%EF%BC%92.png) |
| 30 | ウィンク2 | 2.691511 % | 否 | [![Sour式初音 ウィンク２](images/thumbnails/144/6d4681ca545e0244.png)](images/01_Sour/005_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%EF%BC%92.png) 全半角兼容：ウィンク２ | [![YYB式初音 ウィンク２](images/thumbnails/144/bcb5ad2e5aca9be8.png)](images/02_YYB/018_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%EF%BC%92.png) 全半角兼容：ウィンク２ | 未找到 | [![TDA式初音 ウィンク２](images/thumbnails/144/11331d9f4169d49f.png)](images/04_TDA/005_%E3%82%A6%E3%82%A3%E3%83%B3%E3%82%AF%EF%BC%92.png) 全半角兼容：ウィンク２ |
| 31 | ｷﾘｯ | 2.484472 % | 是 | [![Sour式初音 ｷﾘｯ](images/thumbnails/144/06e62846514cfdb1.png)](images/01_Sour/013_%EF%BD%B7%EF%BE%98%EF%BD%AF.png) | [![YYB式初音 ｷﾘｯ](images/thumbnails/144/9eecd048d87e15f5.png)](images/02_YYB/021_%EF%BD%B7%EF%BE%98%EF%BD%AF.png) | [![Appearance Miku ｷﾘｯ](images/thumbnails/144/b36544f9f30386f1.png)](images/03_Appearance/023_%EF%BD%B7%EF%BE%98%EF%BD%AF.png) | [![TDA式初音 ｷﾘｯ](images/thumbnails/144/c127a5de40112056.png)](images/04_TDA/011_%EF%BD%B7%EF%BE%98%EF%BD%AF.png) |
| 32 | ▲ | 2.484472 % | 是 | [![Sour式初音 ▲E](images/thumbnails/144/180688558ca88dd7.png)](images/01_Sour/083_%E2%96%B2E.png) 候选变体：▲E | 未找到 | [![Appearance Miku ▲](images/thumbnails/144/9f7431d8687fbc98.png)](images/03_Appearance/006_%E2%96%B2.png) | [![TDA式初音 ▲](images/thumbnails/144/486fea67d27bbd23.png)](images/04_TDA/022_%E2%96%B2.png) |
| 33 | ｳｨﾝｸ２右 | 2.277433 % | 是 | [![Sour式初音 ｳｨﾝｸ２右](images/thumbnails/144/b0eb7f42256f7ac2.png)](images/01_Sour/006_%EF%BD%B3%EF%BD%A8%EF%BE%9D%EF%BD%B8%EF%BC%92%E5%8F%B3.png) | [![YYB式初音 ｳｨﾝｸ２右](images/thumbnails/144/dfe804231315a1cc.png)](images/02_YYB/019_%EF%BD%B3%EF%BD%A8%EF%BE%9D%EF%BD%B8%EF%BC%92%E5%8F%B3.png) | 未找到 | [![TDA式初音 ｳｨﾝｸ２右](images/thumbnails/144/2eea3e3e6a1b42ca.png)](images/04_TDA/006_%EF%BD%B3%EF%BD%A8%EF%BE%9D%EF%BD%B8%EF%BC%92%E5%8F%B3.png) |
| 34 | つまさき右 | 2.070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 35 | 涙 | 2.070393 % | 否 | [![Sour式初音 涙](images/thumbnails/144/21db1fdbe4733ff2.png)](images/01_Sour/071_%E6%B6%99.png) | 未找到 | 未找到 | [![TDA式初音 涙](images/thumbnails/144/dba1665c6ff15611.png)](images/04_TDA/039_%E6%B6%99.png) |
| 36 | 口角下げ | 1.863354 % | 是 | [![Sour式初音 口角下げ](images/thumbnails/144/13c49ca4925d715c.png)](images/01_Sour/033_%E5%8F%A3%E8%A7%92%E4%B8%8B%E3%81%92.png) | [![YYB式初音 口角下げ](images/thumbnails/144/2951a537478b291a.png)](images/02_YYB/044_%E5%8F%A3%E8%A7%92%E4%B8%8B%E3%81%92.png) | 未找到 | [![TDA式初音 口角下げ](images/thumbnails/144/70ff8e164abe491b.png)](images/04_TDA/035_%E5%8F%A3%E8%A7%92%E4%B8%8B%E3%81%92.png) |
| 37 | 口横広げ | 1.863354 % | 是 | [![Sour式初音 口横広げ](images/thumbnails/144/369da5964468ee7c.png)](images/01_Sour/034_%E5%8F%A3%E6%A8%AA%E5%BA%83%E3%81%92.png) | [![YYB式初音 口横広げ](images/thumbnails/144/f0a3f10cbb33c044.png)](images/02_YYB/047_%E5%8F%A3%E6%A8%AA%E5%BA%83%E3%81%92.png) | 未找到 | [![TDA式初音 口横広げ](images/thumbnails/144/6fcca19325f0cdc1.png)](images/04_TDA/036_%E5%8F%A3%E6%A8%AA%E5%BA%83%E3%81%92.png) |
| 38 | にやり２ | 1.863354 % | 是 | 未找到 | 未找到 | 未找到 | [![TDA式初音 にやり２](images/thumbnails/144/b93460f65cd1d9a1.png)](images/04_TDA/029_%E3%81%AB%E3%82%84%E3%82%8A%EF%BC%92.png) |
| 39 | 笑 | 1.863354 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 40 | にやり2 | 1.863354 % | 否 | 未找到 | 未找到 | 未找到 | [![TDA式初音 にやり２](images/thumbnails/144/b93460f65cd1d9a1.png)](images/04_TDA/029_%E3%81%AB%E3%82%84%E3%82%8A%EF%BC%92.png) 全半角兼容：にやり２ |
| 41 | ぽけー | 1.656315 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 42 | 驚き | 1.656315 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 43 | 見開き | 1.656315 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 44 | つまさき左 | 1.656315 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 45 | 恐ろしい子！ | 1.449275 % | 是 | [![Sour式初音 恐ろしい子！](images/thumbnails/144/ae74f847071132cc.png)](images/01_Sour/025_%E6%81%90%E3%82%8D%E3%81%97%E3%81%84%E5%AD%90%EF%BC%81.png) | 未找到 | 未找到 | [![TDA式初音 恐ろしい子！](images/thumbnails/144/f198c5e77d13bfce.png)](images/04_TDA/046_%E6%81%90%E3%82%8D%E3%81%97%E3%81%84%E5%AD%90%EF%BC%81.png) |
| 46 | む | 1.449275 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 47 | しいたけ | 1.449275 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 48 | 口わらい | 1.242236 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 49 | △ | 1.242236 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 50 | まば左 | 1.242236 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 51 | 喜ぶ | 1.242236 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 52 | 右ウィンク | 1.242236 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 53 | ｺｯﾁﾐﾝﾅ | 1.035197 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 54 | 困り | 1.035197 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 55 | 口わらい2 | 1.035197 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 56 | ああ | 1.035197 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 57 | 叫び | 1.035197 % | 否 | [![Sour式初音 叫びE](images/thumbnails/144/8a7522477fc5155a.png)](images/01_Sour/086_%E5%8F%AB%E3%81%B3E.png) 候选变体：叫びE | 未找到 | [![Appearance Miku 叫び](images/thumbnails/144/275952d697886626.png)](images/03_Appearance/013_%E5%8F%AB%E3%81%B3.png) | 未找到 |
| 58 | 上右 | 1.035197 % | 否 | [![Sour式初音 上右](images/thumbnails/144/d90a2291baca96c0.png)](images/01_Sour/053_%E4%B8%8A%E5%8F%B3.png) | 未找到 | 未找到 | 未找到 |
| 59 | まば右 | 1.035197 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 60 | つま先左 | 1.035197 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 61 | つま先右 | 1.035197 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 62 | 口下 | 0.8281574 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 63 | ウィンク左 | 0.8281574 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 64 | 平行 | 0.8281574 % | 否 | 未找到 | [![YYB式初音 平行](images/thumbnails/144/f23a4c1560da5b26.png)](images/02_YYB/006_%E5%B9%B3%E8%A1%8C.png) | [![Appearance Miku 平行](images/thumbnails/144/4c7ded4fedadc425.png)](images/03_Appearance/033_%E5%B9%B3%E8%A1%8C.png) | 未找到 |
| 65 | にこ | 0.8281574 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 66 | あ２ | 0.8281574 % | 是 | [![Sour式初音 あ2E](images/thumbnails/144/e354f3a75e5c8760.png)](images/01_Sour/075_%E3%81%822E.png) 候选变体：あ2E | [![YYB式初音 xあ２](images/thumbnails/144/c29badb04763edf9.png)](images/02_YYB/060_x%E3%81%82%EF%BC%92.png) 候选变体：xあ２ | 未找到 | [![TDA式初音 あ２](images/thumbnails/144/7f52b2912d98bd3a.png)](images/04_TDA/020_%E3%81%82%EF%BC%92.png) |
| 67 | －－ | 0.8281574 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 68 | まばたき２ | 0.8281574 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 69 | 前 | 0.621118 % | 否 | 未找到 | 未找到 | [![Appearance Miku 前](images/thumbnails/144/2ae22832ca201519.png)](images/03_Appearance/039_%E5%89%8D.png) | [![TDA式初音 前](images/thumbnails/144/155602a13f30c519.png)](images/04_TDA/055_%E5%89%8D.png) |
| 70 | ライン短 | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 71 | ほ | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 72 | 一文字 | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 73 | あーれー | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 74 | にたり | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 75 | いい | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 76 | 悲しい | 0.621118 % | 否 | [![Sour式初音 悲しい](images/thumbnails/144/206a9391ef57a78a.png)](images/01_Sour/048_%E6%82%B2%E3%81%97%E3%81%84.png) | 未找到 | 未找到 | 未找到 |
| 77 | うう | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 78 | むっ | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 79 | あしへこ | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 80 | 八 | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 81 | がーん | 0.621118 % | 否 | [![Sour式初音 がーん](images/thumbnails/144/0ebfe61a5d3b51d9.png)](images/01_Sour/062_%E3%81%8C%E3%83%BC%E3%82%93.png) | 未找到 | 未找到 | [![TDA式初音 がーん](images/thumbnails/144/9bb3937ea08f1cf1.png)](images/04_TDA/048_%E3%81%8C%E3%83%BC%E3%82%93.png) |
| 82 | Λ | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 83 | ハート | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 84 | ウィンク右２ | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 85 | 泣き | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 86 | 上左 | 0.621118 % | 否 | [![Sour式初音 上左](images/thumbnails/144/5b44ba66674b385c.png)](images/01_Sour/052_%E4%B8%8A%E5%B7%A6.png) | 未找到 | 未找到 | 未找到 |
| 87 | 泣き眉 | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 88 | わー | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 89 | へ | 0.621118 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 90 | えー | 0.621118 % | 否 | 未找到 | 未找到 | [![Appearance Miku えー](images/thumbnails/144/d96077e427443d60.png)](images/03_Appearance/014_%E3%81%88%E3%83%BC.png) | 未找到 |
| 91 | 縮小 | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 92 | はぁと | 0.4140787 % | 是 | [![Sour式初音 はぁと](images/thumbnails/144/4065c1c742456e65.png)](images/01_Sour/020_%E3%81%AF%E3%81%81%E3%81%A8.png) | 未找到 | 未找到 | [![TDA式初音 はぁと](images/thumbnails/144/c93d77a4ddb51379.png)](images/04_TDA/042_%E3%81%AF%E3%81%81%E3%81%A8.png) |
| 93 | 怒り右 | 0.4140787 % | 否 | [![Sour式初音 怒り右](images/thumbnails/144/22ffbdd0e4a729f0.png)](images/01_Sour/047_%E6%80%92%E3%82%8A%E5%8F%B3.png) | 未找到 | 未找到 | 未找到 |
| 94 | どんより | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 95 | 口すぼみ | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 96 | 頬染め | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 97 | おお | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 98 | 困り右 | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 99 | 犬歯 | 0.4140787 % | 否 | [![Sour式初音 犬歯](images/thumbnails/144/9e49d2d45ec54c48.png)](images/01_Sour/067_%E7%8A%AC%E6%AD%AF.png)；头部画面变化很小，待核对；[组合辅助：あE=1 + 犬歯=1](images/01_Sour/context_%E7%8A%AC%E6%AD%AF%2B%E3%81%82E.png) | 未找到 | 未找到 | 未找到 |
| 100 | 赤み | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 101 | ウルウル目 | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 102 | 怒り左 | 0.4140787 % | 否 | [![Sour式初音 怒り左](images/thumbnails/144/a4dfdcb6f7c96a78.png)](images/01_Sour/046_%E6%80%92%E3%82%8A%E5%B7%A6.png) | 未找到 | 未找到 | 未找到 |
| 103 | おー | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 104 | ジト目 | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 105 | ニッ | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 106 | 半開き | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 107 | 下瞼上げ | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 108 | ３ | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 109 | 星目 | 0.4140787 % | 是 | [![Sour式初音 星目](images/thumbnails/144/cd222ee5592637ef.png)](images/01_Sour/021_%E6%98%9F%E7%9B%AE.png) | 未找到 | 未找到 | [![TDA式初音 星目](images/thumbnails/144/7a6af30160d1838e.png)](images/04_TDA/041_%E6%98%9F%E7%9B%AE.png) |
| 110 | □ | 0.4140787 % | 是 | [![Sour式初音 □E](images/thumbnails/144/2c2814a230664d9c.png)](images/01_Sour/084_%E2%96%A1E.png) 候选变体：□E | [![YYB式初音 □](images/thumbnails/144/6c70b78211d9564f.png)](images/02_YYB/035_%E2%96%A1.png) | 未找到 | [![TDA式初音 □](images/thumbnails/144/ab3920492bc57aff.png)](images/04_TDA/024_%E2%96%A1.png) |
| 111 | 左眉上 | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 112 | ◇◇ | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 113 | ○○ | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 114 | 見開く | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 115 | 真っ直ぐ | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 116 | 頬染２ | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 117 | 絶望 | 0.4140787 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 118 | band1 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 119 | 拡大 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 120 | ?? | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 121 |  | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 122 | ? | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 123 | 白目 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 124 | ∧２ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 125 | くっ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 126 | にっ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 127 | 口幅開き | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 128 | 白目黒 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 129 | 瞳赤 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 130 | 青ざめ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 131 | 赤面 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 132 | 汗3 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 133 | ハイライト大 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 134 | 下瞼↑ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 135 | 睨 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 136 | 目尻下 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 137 | 上瞼↓ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 138 | あああ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 139 | いいい | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 140 | にこり右 | 0.2070393 % | 否 | [![Sour式初音 にこり右](images/thumbnails/144/b14c91c667142c15.png)](images/01_Sour/044_%E3%81%AB%E3%81%93%E3%82%8A%E5%8F%B3.png) | 未找到 | 未找到 | 未找到 |
| 141 | コッチミンナ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 142 | 困り左 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 143 | 赤み2 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 144 | グル目 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 145 | 左ほほ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 146 | 右ほほ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 147 | ゴーグル | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 148 | 無表情 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 149 | ウルウル | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 150 | 口下げ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 151 | 涙消し | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 152 | 赤らめ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 153 | アゴ下げ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 154 | 垂れ目 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 155 | ぴえん | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 156 | おちょぼ口 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 157 | すぼめ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 158 | 歯なし | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 159 | ウィンク1 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 160 | 照れ2 | 0.2070393 % | 否 | [![Sour式初音 照れ２](images/thumbnails/144/c738bb0eaf7f3171.png)](images/01_Sour/061_%E7%85%A7%E3%82%8C%EF%BC%92.png) 全半角兼容：照れ２ | 未找到 | 未找到 | 未找到 |
| 161 | シリアス | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 162 | にや | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 163 | に～ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 164 | ぎり | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 165 | 舌細 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 166 | 下L | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 167 | 下R | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 168 | にこ右 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 169 | 頬膨らみ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 170 | ｳｨﾝｸ右２ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 171 | にこ左 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 172 | 顔線 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 173 | ニカッ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 174 | いー | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 175 | Д | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 176 | ω口 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 177 | 瞳大 | 0.2070393 % | 否 | [![Sour式初音 瞳大](images/thumbnails/144/578f4b02f78e9f0b.png)](images/01_Sour/027_%E7%9E%B3%E5%A4%A7.png) | 未找到 | 未找到 | 未找到 |
| 178 | 縞パン | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 179 | ハァ？ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 180 | 目２ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 181 | 暗目 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 182 | はちゅ目 | 0.2070393 % | 是 | [![Sour式初音 はちゅ目](images/thumbnails/144/f30a7475b0d69821.png)](images/01_Sour/015_%E3%81%AF%E3%81%A1%E3%82%85%E7%9B%AE.png) | [![YYB式初音 はちゅ目](images/thumbnails/144/5dceae9df1c009bb.png)](images/02_YYB/030_%E3%81%AF%E3%81%A1%E3%82%85%E7%9B%AE.png) | 未找到 | [![TDA式初音 はちゅ目](images/thumbnails/144/f06865a4c5715f56.png)](images/04_TDA/012_%E3%81%AF%E3%81%A1%E3%82%85%E7%9B%AE.png) |
| 183 | look down | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 184 | look right | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 185 | look left | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 186 | wing | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 187 | 格子開 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 188 | 右眉上 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 189 | わーい | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 190 | sword | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 191 | ぺろっ | 0.2070393 % | 是 | 未找到 | [![YYB式初音 ぺろっ](images/thumbnails/144/77bd6bf92f14cc0b.png)](images/02_YYB/039_%E3%81%BA%E3%82%8D%E3%81%A3.png) | 未找到 | [![TDA式初音 ぺろっ](images/thumbnails/144/a74c221ab97dce40.png)](images/04_TDA/031_%E3%81%BA%E3%82%8D%E3%81%A3.png) |
| 192 | ニヤリ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 193 | ニヤリ左 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 194 | 歯隠し | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 195 | デフォルト口 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 196 | 歯off | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 197 | 悲し目 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 198 | 嬉し目 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 199 | あ３ | 0.2070393 % | 否 | 未找到 | [![YYB式初音 xあ３](images/thumbnails/144/cbbbb565b1b54f7d.png)](images/02_YYB/061_x%E3%81%82%EF%BC%93.png) 候选变体：xあ３ | 未找到 | 未找到 |
| 200 | _笑い２ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 201 | 怒る | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 202 | 下2 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 203 | ｼｬｷｰﾝ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 204 | かなり下 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 205 | 困る左だけ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 206 | 怒り左だけ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 207 | むす | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 208 | あ2 | 0.2070393 % | 否 | [![Sour式初音 あ2E](images/thumbnails/144/e354f3a75e5c8760.png)](images/01_Sour/075_%E3%81%822E.png) 候选变体：あ2E | [![YYB式初音 xあ２](images/thumbnails/144/c29badb04763edf9.png)](images/02_YYB/060_x%E3%81%82%EF%BC%92.png) 候选变体：xあ２ | 未找到 | [![TDA式初音 あ２](images/thumbnails/144/7f52b2912d98bd3a.png)](images/04_TDA/020_%E3%81%82%EF%BC%92.png) 全半角兼容：あ２ |
| 209 | い2 | 0.2070393 % | 否 | [![Sour式初音 い2E](images/thumbnails/144/0b40a337363bb67c.png)](images/01_Sour/077_%E3%81%842E.png) 候选变体：い2E | [![YYB式初音 xい２](images/thumbnails/144/061a11fd3a8b0320.png)](images/02_YYB/064_x%E3%81%84%EF%BC%92.png) 候选变体：xい２ | 未找到 | 未找到 |
| 210 | お2 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 211 | △１ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 212 | んー | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 213 | ＝＝ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 214 | ふむふむ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 215 | ほっ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 216 | □（大） | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 217 | ほほ上 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 218 | 閉じる | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 219 | ニコ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 220 | ワ大 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 221 | 変形 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 222 | ウィンク右2 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 223 | 大口 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 224 | なぬ！ | 0.2070393 % | 否 | [![Sour式初音 なぬ！](images/thumbnails/144/29976ed947880d03.png)](images/01_Sour/014_%E3%81%AA%E3%81%AC%EF%BC%81.png) | 未找到 | [![Appearance Miku なぬ！](images/thumbnails/144/c7814741b9608c9e.png)](images/03_Appearance/027_%E3%81%AA%E3%81%AC%EF%BC%81.png) | 未找到 |
| 225 | ｷﾞｭｯ | 0.2070393 % | 否 | 未找到 | 未找到 | [![Appearance Miku ｷﾞｭｯ](images/thumbnails/144/318dbeb35af26c15.png)](images/03_Appearance/018_%EF%BD%B7%EF%BE%9E%EF%BD%AD%EF%BD%AF.png) | 未找到 |
| 226 | 猫耳 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 227 | 笑い目 | 0.2070393 % | 否 | [![Sour式初音 笑い目](images/thumbnails/144/beafdbe0fe544ff5.png)](images/01_Sour/018_%E7%AC%91%E3%81%84%E7%9B%AE.png) | [![YYB式初音 笑い目](images/thumbnails/144/50b4f8bcc3d31d78.png)](images/02_YYB/032_%E7%AC%91%E3%81%84%E7%9B%AE.png) | [![Appearance Miku 笑い目](images/thumbnails/144/b1b08236dfc5337d.png)](images/03_Appearance/026_%E7%AC%91%E3%81%84%E7%9B%AE.png) | 未找到 |
| 228 | カメラ目線 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 229 | ωあ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 230 | ωお | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 231 | にこっ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 232 | にやり右 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 233 | にやり左 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 234 | ほっぺ斜 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 235 | 一 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 236 | （*?Д｀） | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 237 | 怒り眉 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 238 | 困惑 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 239 | 照れる | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 240 | 激怒 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 241 | いーっ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 242 | じと目2 | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 243 | 困る２ | 0.2070393 % | 否 | 未找到 | [![YYB式初音 困る2](images/thumbnails/144/e53ddff284c302fa.png)](images/02_YYB/003_%E5%9B%B0%E3%82%8B2.png) 全半角兼容：困る2 | 未找到 | 未找到 |
| 244 | ドヤァ | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |
| 245 | ウインク２R | 0.2070393 % | 否 | 未找到 | 未找到 | 未找到 | 未找到 |

## 模型独有项与全部渲染

以下页面列出各模型**全部实际形态键**，包括未出现在 lil 统计主表中的项目，方便下一轮交叉验证。

- [Sour式初音：94 项全部图片](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/01_Sour.md)；其中 39 项未用于主表。
- [YYB式初音：73 项全部图片](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/02_YYB.md)；其中 34 项未用于主表。
- [Appearance Miku：45 项全部图片](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/03_Appearance.md)；其中 14 项未用于主表。
- [TDA式初音：63 项全部图片](%E6%A8%A1%E5%9E%8B%E6%98%8E%E7%BB%86/04_TDA.md)；其中 18 项未用于主表。

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
- `lil统计与模型对应.csv`：按使用率降序排列的 245 × 4 项统计名称与图片映射。
- `预设与模型对应.csv`：按预设原始顺序排列的 55 × 4 项名称映射。
- `render_validation.json`：完整图像核验。
- `render.log`：Blender 渲染日志。
