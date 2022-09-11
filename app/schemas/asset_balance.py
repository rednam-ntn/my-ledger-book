from datetime import datetime

from pydantic import BaseModel


class AssetBalanceBase(BaseModel):
    amount: float


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
