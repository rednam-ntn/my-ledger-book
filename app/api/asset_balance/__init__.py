from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.asset_balance.crud import crud_asset_balance
from app.api.deps import get_db
from app.schemas.asset_balance import AssetBalance, AssetBalanceCreate, AssetBalanceUpdate

router = APIRouter()


@router.get("/{id}", response_model=AssetBalance)
def read_item(
    id: int,
    db: Session = Depends(get_db),
) -> AssetBalance:
    """
    Get asset balance by ID.
    """
    return crud_asset_balance.get(db=db, id=id)


@router.get("/", response_model=List[AssetBalance])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Any:
    """
    Retrieve assets balance.
    """
    return crud_asset_balance.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=AssetBalance)
def create_item(
    asset_balance_in: AssetBalanceCreate,
    db: Session = Depends(get_db),
) -> AssetBalance:
    """
    Create new asset balance.
    """
    return crud_asset_balance.create(db=db, obj_in=asset_balance_in)


@router.put("/{id}", response_model=AssetBalance)
def update_item(
    id: int,
    asset_balance_in: AssetBalanceUpdate,
    db: Session = Depends(get_db),
) -> AssetBalance:
    """
    Update an asset balance.
    """
    asset = crud_asset_balance.get(db=db, id=id)
    return crud_asset_balance.update(db=db, db_obj=asset, obj_in=asset_balance_in)


@router.delete("/{id}", response_model=AssetBalance)
def delete_item(
    id: int,
    db: Session = Depends(get_db),
) -> AssetBalance:
    """
    Delete an asset balance.
    """
    return crud_asset_balance.remove(db=db, id=id)
