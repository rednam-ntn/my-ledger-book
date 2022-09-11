from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.asset_price.crud import crud_asset_price
from app.api.deps import get_db
from app.schemas.asset_price import AssetPrice, AssetPriceCreate, AssetPriceUpdate

router = APIRouter()


@router.get("/{id}", response_model=AssetPrice)
def read_item(
    id: int,
    db: Session = Depends(get_db),
) -> AssetPrice:
    """
    Get asset price by ID.
    """
    return crud_asset_price.get(db=db, id=id)


@router.get("/", response_model=List[AssetPrice])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Any:
    """
    Retrieve assets price.
    """
    return crud_asset_price.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=AssetPrice)
def create_item(
    asset_price_in: AssetPriceCreate,
    db: Session = Depends(get_db),
) -> AssetPrice:
    """
    Create new asset price.
    """
    return crud_asset_price.create(db=db, obj_in=asset_price_in)


@router.put("/{id}", response_model=AssetPrice)
def update_item(
    id: int,
    asset_price_in: AssetPriceUpdate,
    db: Session = Depends(get_db),
) -> AssetPrice:
    """
    Update an asset price.
    """
    asset = crud_asset_price.get(db=db, id=id)
    return crud_asset_price.update(db=db, db_obj=asset, obj_in=asset_price_in)


@router.delete("/{id}", response_model=AssetPrice)
def delete_item(
    id: int,
    db: Session = Depends(get_db),
) -> AssetPrice:
    """
    Delete an asset price.
    """
    return crud_asset_price.remove(db=db, id=id)
