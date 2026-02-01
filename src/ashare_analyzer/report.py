from __future__ import annotations

from datetime import date
from typing import Iterable

from .models import SectorSummary, StockRecommendation


def render_report(
    trade_date: date | None,
    sector_summaries: Iterable[SectorSummary],
    recommendations: Iterable[StockRecommendation],
) -> str:
    title_date = trade_date.isoformat() if trade_date else "最近交易日"
    lines: list[str] = [f"# A股板块行情与推荐 ({title_date})", ""]

    lines.append("## 板块行情概览")
    lines.append("| 板块 | 平均涨跌幅 | 成交量(亿) | 波动率 |")
    lines.append("| --- | --- | --- | --- |")
    for summary in sector_summaries:
        lines.append(
            "| {sector} | {avg:.2f}% | {volume:.2f} | {vol:.2f} |".format(
                sector=summary.sector,
                avg=summary.avg_change_pct,
                volume=summary.total_volume / 1e8,
                vol=summary.volatility,
            )
        )

    lines.append("")
    lines.append("## 推荐股票")
    lines.append("| 代码 | 名称 | 板块 | 涨跌幅 | 推荐理由 |")
    lines.append("| --- | --- | --- | --- | --- |")

    recommendation_list = list(recommendations)
    if not recommendation_list:
        lines.append("| - | - | - | - | 暂无满足条件的推荐 |")
    else:
        for item in recommendation_list:
            lines.append(
                "| {ticker} | {name} | {sector} | {change:.2f}% | {reason} |".format(
                    ticker=item.ticker,
                    name=item.name,
                    sector=item.sector,
                    change=item.change_pct,
                    reason=item.reason,
                )
            )

    lines.append("")
    lines.append("## 风险提示")
    lines.append("以上分析仅基于历史行情数据样本，不构成投资建议。请结合自身风险承受能力审慎决策。")

    return "\n".join(lines)
