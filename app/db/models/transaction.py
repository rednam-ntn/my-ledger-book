from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db import Base


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    from_account_id = Column(Integer, ForeignKey("account.id"), nullable=True)
    from_account = relationship("Account", back_populates="transactions_out")

    to_account_id = Column(Integer, ForeignKey("account.id"), nullable=True)
    to_account = relationship("Account", back_populates="transactions_in")

    asset_id = Column(Integer, ForeignKey("asset.id"))
    asset = relationship("Asset", back_populates="transactions")

    price_id = Column(Integer, ForeignKey("asset_price.id"))
    price = relationship("AssetPrice", back_populates="transactions")
