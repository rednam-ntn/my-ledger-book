from pathlib import Path
from typing import Optional

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel

from app.core import INPUT_PATH, settings

router = APIRouter(prefix="/asset", tags=["asset"])


@router.get("/{asset_id}")
async def get_asset(asset_id: str):
    return asset_id
