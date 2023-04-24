from __future__ import annotations

import datetime
import re

from clinton.models.map_file import MapResult


def parse_date(date: str) -> datetime.date:
    if re.match(r"\d{1,2}/\d{1,2}/\d{4}", date):
        return datetime.datetime.strptime(date, "%m/%d/%Y").date()
    if re.match(r"\d{4}-\d{1,2}-\d{1,2}", date):
        return datetime.datetime.strptime(date, "%Y-%m-%d").date()
    if re.match(r"\w+ \d+[,a-z]{1,2} \d+", date):
        date = re.sub("(st|nd|rd|th) ", ", ", date)
        if len(date.split()[0]) == 3:
            fmt = "%b %d, %Y"
        fmt = "%B %d, %Y"
        return datetime.datetime.strptime(date, fmt).date()
    raise ValueError(f"Unknown date format: {date}")


def process_date(mr: MapResult | None) -> datetime.date | None:
    if mr is None:
        return None
    date = mr["date"]
    try:
        return parse_date(date)
    except ValueError:
        print(f"Unknown date format: {date!r} in {mr!r}")
        return None
