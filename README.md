# A股板块行情分析与推荐工具

该项目提供一个可扩展的本地化分析工具，用于汇总每日 A 股板块行情、生成报告并给出候选推荐股票。当前版本内置示例数据，便于快速体验。

## 功能亮点

- 板块涨跌幅、成交量与波动率统计
- 根据板块强度与个股涨幅输出推荐名单
- 生成 Markdown 报告，便于分享与归档
- 完全本地运行，可替换为真实行情数据源

## 目录结构

```
.
├── data
│   └── sample_market.csv    # 示例行情数据
└── src
    └── ashare_analyzer       # 核心分析模块
```

## 快速开始

使用内置示例数据生成报告：

```bash
PYTHONPATH=src python -m ashare_analyzer --data data/sample_market.csv --date 2024-01-02
```

保存报告到文件：

```bash
PYTHONPATH=src python -m ashare_analyzer --data data/sample_market.csv --date 2024-01-02 --output report.md
```

## 数据格式

输入 CSV 需包含以下字段：

- `date`: 交易日期（YYYY-MM-DD）
- `sector`: 板块名称
- `ticker`: 证券代码
- `name`: 股票名称
- `close`: 收盘价
- `change_pct`: 涨跌幅（%）
- `volume`: 成交量

## 后续可扩展方向

- 接入实时行情 API（如券商/第三方数据源）
- 引入多因子评分与风控指标
- 增加定时任务与可视化仪表盘

> 风险提示：本工具仅用于数据分析和演示，不构成投资建议。
