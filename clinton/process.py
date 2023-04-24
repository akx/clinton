from __future__ import annotations

from pdfminer.high_level import extract_text

from clinton.models.map_file import get_map
from clinton.models.result import Result
from clinton.parsers.date_parser import process_date
from clinton.parsers.money_parser import process_money


def process_file(filename: str, print_text: bool) -> Result:
    text = extract_text(filename)
    if print_text:
        print(text)
    vendor = get_map("vendor").find(text)
    document_date = process_date(get_map("document_date").find(text))
    payment_date = process_date(get_map("payment_date").find(text))
    payment_money = process_money(get_map("payment_amount").find(text))
    if payment_money is not None:
        payment_amount, payment_currency = payment_money
    else:
        payment_amount = None
        payment_currency = None
    return Result(
        filename=filename,
        text=text,
        vendor_name=str(vendor) if vendor else None,
        document_date=document_date,
        payment_date=payment_date,
        payment_amount=payment_amount,
        payment_currency=payment_currency,
    )
