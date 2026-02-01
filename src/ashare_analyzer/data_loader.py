from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import Iterable

from .models import StockRecord


def load_market_data(path: str | Path) -> list[StockRecord]:
    records: list[StockRecord] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            trade_date = datetime.strptime(row["date"], "%Y-%m-%d").date()
            records.append(
                StockRecord(
                    trade_date=trade_date,
                    sector=row["sector"],
                    ticker=row["ticker"],
                    name=row["name"],
                    close=float(row["close"]),
                    change_pct=float(row["change_pct"]),
                    volume=float(row["volume"]),
                )
            )
    return records


def filter_by_date(records: Iterable[StockRecord], target_date: str | None) -> list[StockRecord]:
    if target_date is None:
        return list(records)
    desired = datetime.strptime(target_date, "%Y-%m-%d").date()
    return [record for record in records if record.trade_date == desired]
