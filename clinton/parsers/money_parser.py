from __future__ import annotations

from decimal import Decimal

from clinton.models.map_file import MapResult


def process_money(mr: MapResult | None) -> tuple[Decimal, str] | None:
    if mr is None:
        return None
    amount = mr["amount"]
    currency = mr["currency"]
    if "," in amount and "." in amount:
        amount = amount.replace(",", "")
    elif "," in amount and "." not in amount:
        amount = amount.replace(",", ".")
    if amount.startswith("$"):
        currency = "USD"
        amount = amount[1:]
    elif amount.startswith("€"):
        currency = "EUR"
        amount = amount[1:]

    return Decimal(amount), currency
