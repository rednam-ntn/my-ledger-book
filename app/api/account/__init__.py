from pathlib import Path
from typing import Optional

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel

router = APIRouter()


@router.get("/{account_id}")
async def get_account(account_id: str):
    return account_id
