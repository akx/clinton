from __future__ import annotations

import dataclasses
import datetime
import os
from decimal import Decimal


@dataclasses.dataclass
class Result:
    filename: str
    text: str
    vendor_name: str | None
    document_date: datetime.date | None
    payment_date: datetime.date | None
    payment_amount: Decimal | None
    payment_currency: str | None

    def to_dict(self) -> dict[str, str | datetime.date | None]:
        d = dataclasses.asdict(self)
        d.pop("text")
        return d

    def get_new_filename(self) -> str:
        stem, ext = os.path.splitext(os.path.basename(self.filename))
        bits = []
        if self.vendor_name:
            bits.append(self.vendor_name)
        else:
            bits.append(stem)
        if self.document_date:
            bits.append(self.document_date.strftime("%Y-%m-%d"))
        if self.payment_date:
            bits.append(self.payment_date.strftime("%Y-%m-%d"))
        if self.payment_amount:
            bits.append(str(self.payment_amount))
        if self.payment_currency:
            bits.append(self.payment_currency)
        return "_".join(bits) + ext
