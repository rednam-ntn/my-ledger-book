from pathlib import Path
from typing import Optional

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel

from app.core import INPUT_PATH, settings

router = APIRouter(prefix="/account", tags=["account"])


@router.get("/{account_id}")
async def get_account(account_id: str):
    return account_id
