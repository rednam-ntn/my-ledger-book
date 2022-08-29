from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base
from app.schemas.asset import AssetType


class Asset(Base):
    __tablename__ = "asset"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(Enum(AssetType), default=AssetType.cash, nullable=False)

    description_vi = Column(String, nullable=True)
    description_en = Column(String, nullable=True)
    url = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    asset_supplier_id = Column(Integer, ForeignKey("asset_supplier.id"), nullable=True)
    asset_supplier = relationship("AssetSupplier", back_populates="assets")

    prices = relationship("AssetPrice", back_populates="asset")

    assets_balance = relationship("AssetBalance", back_populates="asset")

    transactions = relationship("Transaction", back_populates="asset")
