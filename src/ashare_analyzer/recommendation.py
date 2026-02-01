from __future__ import annotations

from typing import Iterable

from .models import SectorSummary, StockRecord, StockRecommendation


DEFAULT_SECTOR_THRESHOLD = 0.5
DEFAULT_STOCK_THRESHOLD = 2.0


def recommend_stocks(
    records: Iterable[StockRecord],
    sector_summaries: Iterable[SectorSummary],
    sector_threshold: float = DEFAULT_SECTOR_THRESHOLD,
    stock_threshold: float = DEFAULT_STOCK_THRESHOLD,
) -> list[StockRecommendation]:
    sector_map = {summary.sector: summary for summary in sector_summaries}
    recommendations: list[StockRecommendation] = []

    for record in records:
        summary = sector_map.get(record.sector)
        if summary is None:
            continue
        if summary.avg_change_pct < sector_threshold:
            continue
        if record.change_pct < stock_threshold:
            continue
        volatility_note = "波动温和" if summary.volatility <= 1.5 else "波动较大"
        reason = (
            f"所在板块平均涨幅{summary.avg_change_pct:.2f}%且放量表现，"
            f"个股当日涨幅{record.change_pct:.2f}%，{volatility_note}"
        )
        recommendations.append(
            StockRecommendation(
                ticker=record.ticker,
                name=record.name,
                sector=record.sector,
                change_pct=record.change_pct,
                reason=reason,
            )
        )

    return sorted(recommendations, key=lambda item: item.change_pct, reverse=True)
