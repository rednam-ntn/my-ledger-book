from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description_vi = Column(String)
    description_en = Column(String)
    url = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    transactions_out = relationship(
        "Transaction", back_populates="from_account", foreign_keys="Transaction.from_account_id"
    )
    transactions_in = relationship("Transaction", back_populates="to_account", foreign_keys="Transaction.to_account_id")

    assets_balance = relationship("AssetBalance", back_populates="account")
