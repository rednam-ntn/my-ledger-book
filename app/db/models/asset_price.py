from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db import Base


class AssetPrice(Base):
    __tablename__ = "asset_price"

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    asset_id = Column(Integer, ForeignKey("asset.id"), nullable=False)
    asset = relationship("Asset", back_populates="prices")

    transactions = relationship("Transaction", back_populates="price")
