from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AccountBase(BaseModel):
    name: Optional[str]
    description_vi: Optional[str]
    description_en: Optional[str]
    url: Optional[str]


class AccountCreate(AccountBase):
    name: str


class AccountUpdate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    name: str

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
