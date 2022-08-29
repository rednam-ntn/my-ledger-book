from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.schemas.asset import Asset


class AssetSupplierBase(BaseModel):
    name: Optional[str]
    description: Optional[str] = None
    url: Optional[str] = None

    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class AssetSupplierCreate(AssetSupplierBase):
    name: str


class AssetSupplierUpdate(AssetSupplierBase):
    pass


class AssetSupplier(AssetSupplierBase):
    id: int
    name: str

    created_at: datetime
    updated_at: datetime

    assets: List[Asset] = []

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
