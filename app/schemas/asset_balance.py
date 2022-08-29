from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AssetBalanceBase(BaseModel):
    amount: float
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class AssetBalanceCreate(AssetBalanceBase):
    pass


class AssetBalanceUpdate(AssetBalanceBase):
    pass


class AssetBalance(AssetBalanceBase):
    id: int

    created_at: datetime
    updated_at: datetime

    account_id: int
    asset_id: int

    class Config:
        orm_mode = True
