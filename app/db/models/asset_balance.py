from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db import Base


class AssetBalance(Base):
    __tablename__ = "asset_balance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    account_id = Column(Integer, ForeignKey("account.id"), nullable=False)
    account = relationship("Account", back_populates="assets_balance")

    asset_id = Column(Integer, ForeignKey("asset.id"), nullable=False)
    asset = relationship("Asset", back_populates="assets_balance")
