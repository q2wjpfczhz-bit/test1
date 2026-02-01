from __future__ import annotations

from collections import defaultdict
from statistics import mean, pstdev
from typing import Iterable

from .models import SectorSummary, StockRecord


def summarize_sectors(records: Iterable[StockRecord]) -> list[SectorSummary]:
    grouped: dict[str, list[StockRecord]] = defaultdict(list)
    for record in records:
        grouped[record.sector].append(record)

    summaries: list[SectorSummary] = []
    for sector, sector_records in grouped.items():
        changes = [record.change_pct for record in sector_records]
        total_volume = sum(record.volume for record in sector_records)
        summaries.append(
            SectorSummary(
                sector=sector,
                avg_change_pct=mean(changes),
                total_volume=total_volume,
                volatility=pstdev(changes) if len(changes) > 1 else 0.0,
            )
        )

    return sorted(summaries, key=lambda item: item.avg_change_pct, reverse=True)
