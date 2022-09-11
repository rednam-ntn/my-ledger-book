from typing import Any, List

from fastapi import APIRouter, Depends
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
    return crud_asset.get(db=db, id=id)


@router.get("/", response_model=List[Asset])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Any:
    """
    Retrieve assets.
    """
    return crud_asset.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=Asset)
def create_item(
    asset_in: AssetCreate,
    db: Session = Depends(get_db),
) -> Asset:
    """
    Create new asset.
    """
    return crud_asset.create(db=db, obj_in=asset_in)


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
    return crud_asset.update(db=db, db_obj=asset, obj_in=asset_in)


@router.delete("/{id}", response_model=Asset)
def delete_item(
    id: int,
    db: Session = Depends(get_db),
) -> Asset:
    """
    Delete an asset.
    """
    return crud_asset.remove(db=db, id=id)
