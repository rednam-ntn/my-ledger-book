from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.asset_supplier.crud import crud_asset_supplier
from app.api.deps import get_db
from app.schemas.asset_supplier import AssetSupplier, AssetSupplierCreate, AssetSupplierUpdate

router = APIRouter()


@router.get("/{id}", response_model=AssetSupplier)
def read_item(
    id: int,
    db: Session = Depends(get_db),
) -> AssetSupplier:
    """
    Get asset supplier by ID.
    """
    return crud_asset_supplier.get(db=db, id=id)


@router.get("/", response_model=List[AssetSupplier])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Any:
    """
    Retrieve assets supplier.
    """
    return crud_asset_supplier.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=AssetSupplier)
def create_item(
    asset_supplier_in: AssetSupplierCreate,
    db: Session = Depends(get_db),
) -> AssetSupplier:
    """
    Create new asset supplier.
    """
    return crud_asset_supplier.create(db=db, obj_in=asset_supplier_in)


@router.put("/{id}", response_model=AssetSupplier)
def update_item(
    id: int,
    asset_supplier_in: AssetSupplierUpdate,
    db: Session = Depends(get_db),
) -> AssetSupplier:
    """
    Update an asset supplier.
    """
    asset = crud_asset_supplier.get(db=db, id=id)
    return crud_asset_supplier.update(db=db, db_obj=asset, obj_in=asset_supplier_in)


@router.delete("/{id}", response_model=AssetSupplier)
def delete_item(
    id: int,
    db: Session = Depends(get_db),
) -> AssetSupplier:
    """
    Delete an asset supplier.
    """
    return crud_asset_supplier.remove(db=db, id=id)
