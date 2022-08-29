from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.schemas.transaction import Transaction


class AssetPriceBase(BaseModel):
    price: float
    created_at: Optional[datetime]


class AssetPriceCreate(AssetPriceBase):
    asset_id: int


class AssetUpdate(AssetPriceBase):
    pass


class AssetPrice(AssetPriceBase):
    id: int
    asset_id: int
    transactions: List[Transaction] = []

    class Config:
        orm_mode = True
