from pathlib import Path
from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.api.asset.crud import crud_asset
from app.api.deps import get_db
from app.schemas.asset import Asset, AssetCreate, AssetUpdate

router = APIRouter()


@router.get("/{id}", response_model=Asset)
def read_item(
    id: int,
    db: Session = Depends(get_db),
) -> Asset:
    """
    Get asset by ID.
    """
    asset = crud_asset.get(db=db, id=id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    return asset


@router.get("/", response_model=List[Asset])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Any:
    """
    Retrieve assets.
    """
    assets = crud_asset.get_multi(db, skip=skip, limit=limit)
    return assets


@router.post("/", response_model=Asset)
def create_item(
    asset_in: AssetCreate,
    db: Session = Depends(get_db),
) -> Asset:
    """
    Create new asset.
    """
    asset = crud_asset.create(db=db, obj_in=asset_in)
    return asset


@router.put("/{id}", response_model=Asset)
def update_item(
    id: int,
    asset_in: AssetUpdate,
    db: Session = Depends(get_db),
) -> Asset:
    """
    Update an asset.
    """
    asset = crud_asset.get(db=db, id=id)
    asset = crud_asset.update(db=db, db_obj=asset, obj_in=asset_in)
    return asset


@router.delete("/{id}", response_model=Asset)
def delete_item(
    id: int,
    db: Session = Depends(get_db),
) -> Asset:
    """
    Delete an asset.
    """
    item = crud_asset.remove(db=db, id=id)
    return item
