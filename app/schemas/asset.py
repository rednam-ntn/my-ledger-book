from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from app.schemas.asset_balance import AssetBalance
from app.schemas.asset_price import AssetPrice
from app.schemas.transaction import Transaction


class AssetType(str, Enum):
    fund = "Fund"
    etf = "ETF"
    stock = "Stock"
    cash = "Cash"


class AssetBase(BaseModel):
    name: Optional[str] = None
    type: Optional[AssetType] = None

    description_vi: Optional[str] = None
    description_en: Optional[str] = None
    url: Optional[str] = None


class AssetCreate(AssetBase):
    name: str
    type: AssetType


class AssetUpdate(AssetBase):
    pass


class Asset(AssetBase):
    id: int
    name: str
    type: AssetType

    created_at: datetime
    updated_at: datetime

    asset_supplier_id: Optional[int]
    prices: List[AssetPrice] = []
    assets_balance: List[AssetBalance] = []
    transactions: List[Transaction] = []

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
