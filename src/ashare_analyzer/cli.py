from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from .analysis import summarize_sectors
from .data_loader import filter_by_date, load_market_data
from .recommendation import recommend_stocks
from .report import render_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A股板块行情分析与推荐工具")
    parser.add_argument("--data", required=True, help="行情数据CSV路径")
    parser.add_argument("--date", help="指定交易日(YYYY-MM-DD)，默认使用数据内全部日期")
    parser.add_argument("--output", help="输出报告文件路径(可选)")
    parser.add_argument("--sector-threshold", type=float, default=0.5, help="板块涨幅阈值")
    parser.add_argument("--stock-threshold", type=float, default=2.0, help="个股涨幅阈值")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    records = load_market_data(args.data)
    filtered = filter_by_date(records, args.date)
    if not filtered:
        raise SystemExit("未找到指定日期的数据")

    summaries = summarize_sectors(filtered)
    recommendations = recommend_stocks(
        filtered,
        summaries,
        sector_threshold=args.sector_threshold,
        stock_threshold=args.stock_threshold,
    )
    trade_date = filtered[0].trade_date if args.date else None
    report = render_report(trade_date, summaries, recommendations)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
