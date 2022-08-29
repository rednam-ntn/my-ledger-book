from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount: float
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    from_account_id: Optional[int]
    to_account_id: Optional[int]

    asset_id: int
    price_id: int

    class Config:
        orm_mode = True
