# Layoff Research Skills

**把裁员公告和上市公司披露，整理成可追溯、可持续更新的研究数据。**

本项目提供两个可安装的 AI skills：一个追踪裁员公告及公司背景，一个采集上市公司的 HR、AI/技术和财务披露。数据采集、字段编码、来源核验和 Excel 导出都按内置定义执行，方便研究者重复使用。

当前版本：**v0.9.0** · Python **3.10+** · 支持 **WorkBuddy / WorkBuddy AI / Codex**

[下载完整源码](layoff-research-skills-v0.9.0-github.zip) · [安装脚本](quick_install.py) · [快速开始](#快速开始) · [数据与审查口径](#数据与审查口径)

## 两个技能分别做什么

| 技能 | 适用任务 | 主要内容 | 默认输出粒度 |
| --- | --- | --- | --- |
| `layoff-announcement-tracker` | 追踪某些公司何时宣布裁员，以及公告如何解释裁员 | 原公告、人数/比例、所述原因、并购、领导变更、公司历史/规模、产品与商业模式、受影响群体 | 每个独立裁员计划一行 |
| `listed-filing-extractor` | 持续整理上市公司的年度披露 | HR与裁员、AI/技术、财务及高管薪酬相关披露 | 每个公司每个财年一行 |

两份 Excel 都只有一张 **“结果”** 工作表，保留字段值、缺失/待审状态与证据。输出模板、字段字典、来源清单模板及编码定义随技能一起安装，其他使用者无需拥有作者的原始 Excel 或聊天记录。

### ① 裁员公告与事件追踪

默认公告窗口为 **2020-01-01 至 2026-09-30**，可按请求修改。上市、私人及已退市公司均可入样本。

- 从裁员 tracker、公司官网、SEC 8-K/6-K、交易所公告和可靠新闻发现候选并追溯原公告。
- 保存公告日、生效期间、人数与比例的上下界、近似表述及分母。
- 记录公司所述原因原文，并用 **8 类可空 0/1 原因码**标记 AI、新技术、财务、运营、并购、战略重组、IPO目标、领导变更；多个原因可同时出现。
- 提取并购/领导更替背景、成立年份、历史、事件时点规模、产品服务、商业模式及实际披露的受影响群体。
- 同一计划的多篇新闻、原公告和申报相互链接；两个独立裁员轮次保留不同计划 ID。

默认文件：`1_layoff_announcements.xlsx`。51 个研究字段，另附身份、状态与证据列。

### ② 上市公司年度披露采集

默认财年为 **FY2019–FY2025**，可按请求修改。稳定 `company_id` 用于连接公告与年度表，缺年报的公司年仍保留。

| 类别 | 字段示例 |
| --- | --- |
| HR与裁员 | 员工总数/构成、培训与开发、人才竞争、劳动风险、留任/流失、人员重组叙事、相关费用 |
| AI与技术 | 产品、内部整合、技术采用、风险、投资/运营支出、R&D、资本化软件及明确AI专项金额 |
| 财务 | 营收、经营利润、净利润、资产负债、重组费用、薪酬费用及相关高管薪酬披露 |

共 **142 个研究字段**：88 个原变量 + 48 个文本披露 0/1 伴随列 + 6 个明确专项金额列。原文、数值和披露编码分别保存。

默认文件：`2_listed_company_filings.xlsx`。

## 数据来源与采集方式

| 来源 | 本版路径 |
| --- | --- |
| SEC EDGAR | 内置历史索引、原文与候选提取流程；年度正本/Proxy保留对应财年，8-K/6-K保留事件候选 |
| 公司官网及可靠新闻 | 由运行技能的代理使用宿主搜索/浏览能力发现链接，随后导入、存快照和核查 |
| layoffs.fyi 等裁员 tracker | 用于发现候选与原链接；实际覆盖情况需报告 |
| HKEX、LSE、ASX、KRX、Xetra | 发现交易所或发行人官方报告后，按来源清单导入 HTML/TXT/PDF |
| 40-F及附件、扫描报告 | 按实际官方报告导入；扫描图片需要实际 OCR/视觉核查 |

其他交易所和 tracker 的发现依赖宿主可用的搜索/浏览工具，本版没有实现各站点的全站私有 API。页面不可访问、缺报告或图片待审时会保留具体缺口。

## 一键安装

在你希望安装技能的电脑上打开终端。需要 **Python 3.10+**，并能访问 GitHub 和 Python 软件包源。

### macOS / Linux

**WorkBuddy：**

```bash
curl -fsSL https://raw.githubusercontent.com/liujinyu42/layoff-research-skills/main/quick_install.py -o quick_install.py && python3 quick_install.py --target workbuddy
```

**WorkBuddy AI：**

```bash
curl -fsSL https://raw.githubusercontent.com/liujinyu42/layoff-research-skills/main/quick_install.py -o quick_install.py && python3 quick_install.py --target workbuddy-ai
```

**Codex：**

```bash
curl -fsSL https://raw.githubusercontent.com/liujinyu42/layoff-research-skills/main/quick_install.py -o quick_install.py && python3 quick_install.py --target codex
```

### Windows PowerShell

以下示例安装到 WorkBuddy；使用其他宿主时替换 `--target`：

```powershell
Invoke-WebRequest 'https://raw.githubusercontent.com/liujinyu42/layoff-research-skills/main/quick_install.py' -OutFile quick_install.py
py -3 quick_install.py --target workbuddy
```

Windows 路径已在脚本中适配；当前验证在 macOS 完成，未完成 Windows 宿主实测。

### 安装脚本会做什么

1. 下载仓库中固定提交的 v0.9.0 源码 ZIP，核对 SHA-256 后解压。
2. 创建项目专用 Python 虚拟环境并安装依赖，保持系统 Python 环境独立。
3. 安装两个自包含技能，并为其命令入口绑定该 Python 环境。
4. 检查两个命令入口，保存完整首次使用提示词。

| `--target` | 默认技能目录 |
| --- | --- |
| `workbuddy` | `~/.workbuddy/skills/` |
| `workbuddy-ai` | `~/.workbuddy-ai/skills/` |
| `codex` | `~/.codex/skills/` |

安装完成后刷新宿主的技能列表，或关闭并重新打开宿主。**安装只部署工具，数据采集在你明确调用技能后开始。**

### 查看计划、升级和自定义位置

```bash
# 下载脚本后，只查看计划
python3 quick_install.py --target workbuddy --dry-run

# 备份并替换同名技能；先结束正在使用它们的任务
python3 quick_install.py --target workbuddy --force

# 指定技能目录及持久运行环境目录
python3 quick_install.py --dest ./my-skills --home ./research-runtime
```

升级会备份两个同名技能目录。已有其他技能保留。`--home` 保存运行环境，安装后请保留该目录。

### 手动安装

下载并解压[完整源码 ZIP](layoff-research-skills-v0.9.0-github.zip)，进入解压目录，在你自己的 Python 虚拟环境中运行：

```bash
python -m pip install -r requirements.txt
python install.py --target workbuddy
```

手动安装时，后续采集命令也应使用已安装这些依赖的 Python 环境。源码包内的 `prompts/first-run.zh-CN.md` 提供完整版首次调用模板。

## 快速开始

### 1. 准备样本名单

公司清单至少包含 `company_id`、`company`；美国申报人补充 CIK，其他市场补充交易所。已退市公司保留历史身份。

```csv
company_id,company,cik,ticker,exchange,listing_status
apple,Apple Inc.,0000320193,AAPL,NASDAQ,listed
```

这是一行格式示例。你可提供自己的公司/事件清单，技能据此建立本次范围。

### 2. 把这段话发给你的 AI 助手

替换方括号内容即可，单独使用一个技能时保留对应任务：

```text
请使用 layoff-announcement-tracker 和 listed-filing-extractor。
公司清单：[公司清单CSV的绝对路径]
公告窗口：2020-01-01至2026-09-30。
年度披露范围：样本上市/已退市公司的FY2019–FY2025。
事件工作区：[绝对路径A]；年度披露工作区：[绝对路径B]。
输出目录：[绝对路径]。
SEC联系信息：[我本人允许使用的ASCII联系人及邮箱]。

按两个skill内置模板与定义采集全部字段。请实际发现来源、阅读原文、
完成首轮与第二次核查，并修复已发现的问题。优先复用有效缓存与判断。

生成1_layoff_announcements.xlsx和2_listed_company_filings.xlsx，
各一张“结果”表。前者每独立计划一行，后者每公司每财年一行。
未解决的来源或字段保留null和原因，检查版标PARTIAL；列出实际缺口。
只在实际审查和覆盖通过后标COMPLETE，不以任务派发成功代替审查。
```

### 3. 后续更新

再次调用时提供原工作区。技能可复用有效快照和判断，仅对新来源、修订文本或失效判定继续处理。定期执行可由你另行授权宿主的调度功能；本项目安装时不启动后台任务。

## 数据与审查口径

- **1 / 0 / null 有不同含义**：1 为符合定义的披露；0 需要实际完整范围的负判；无来源、未审或无法判断保留 null。二元披露码不替代金额、人数或比率。
- **所述原因与经济因果分开**：公司提到 AI 不自动证明 AI 导致裁员，也不预设 AI 是“借口”。
- **金额统一基础货币并保留原值与倍率**：例如 2088 million 对应 2,088,000,000；币种、期间、公司合计/分项、费用/支付/余额分别核查。
- **来源可以回查**：保存快照、正文、哈希、字段引文、偏移/页码映射、判断依据及审查状态。
- **已知错误会阻止导出**：包括原文/编码矛盾、来源损坏、日期无效及二读记录失效；缺口可显式导出 PARTIAL 检查表。

`COMPLETE` 表示本次登记范围与定义下的审查完成；同模型二读属于自审，不能作为独立人工信度。结果仍应由研究者结合原文评估。

## 验证、版本和项目文件

v0.9.0 已完成 **20 项离线测试**，并检查双技能独立安装、SEC 合成样本链路、PDF 两页文本/页码映射及两套单表模板。安装入口另做本地验证；GitHub/PyPI网络可达性取决于运行环境。本项目没有预置真实完整研究样本。

完整源码 ZIP 内包含：

```text
layoff-research-skills/
├── skills/          # 两个技能与模板、字典、定义
├── shared/          # 来源、判定、审查和导出模块
├── engine/          # 内置SEC候选解析库
├── prompts/         # 完整首次使用提示词
├── tests/           # 离线回归测试
├── docs/            # 验证范围
├── install.py
├── requirements.txt
├── CHANGELOG.md
└── LICENSE
```

源码包内许可证为 MIT。仓库首页和安装入口独立更新，源码 ZIP 仍为经过验证的 v0.9.0 版本。
