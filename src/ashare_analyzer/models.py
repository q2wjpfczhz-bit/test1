from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class StockRecord:
    trade_date: date
    sector: str
    ticker: str
    name: str
    close: float
    change_pct: float
    volume: float


@dataclass(frozen=True)
class SectorSummary:
    sector: str
    avg_change_pct: float
    total_volume: float
    volatility: float


@dataclass(frozen=True)
class StockRecommendation:
    ticker: str
    name: str
    sector: str
    change_pct: float
    reason: str
