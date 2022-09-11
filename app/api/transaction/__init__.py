from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.transaction.crud import crud_transaction
from app.schemas.transaction import Transaction, TransactionCreate, TransactionUpdate

router = APIRouter()


@router.get("/{id}", response_model=Transaction)
def read_item(
    id: int,
    db: Session = Depends(get_db),
) -> Transaction:
    """
    Get asset balance by ID.
    """
    return crud_transaction.get(db=db, id=id)


@router.get("/", response_model=List[Transaction])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Any:
    """
    Retrieve assets balance.
    """
    return crud_transaction.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=Transaction)
def create_item(
    transaction_in: TransactionCreate,
    db: Session = Depends(get_db),
) -> Transaction:
    """
    Create new asset balance.
    """
    return crud_transaction.create(db=db, obj_in=transaction_in)


@router.put("/{id}", response_model=Transaction)
def update_item(
    id: int,
    transaction_in: TransactionUpdate,
    db: Session = Depends(get_db),
) -> Transaction:
    """
    Update an asset balance.
    """
    asset = crud_transaction.get(db=db, id=id)
    return crud_transaction.update(db=db, db_obj=asset, obj_in=transaction_in)


@router.delete("/{id}", response_model=Transaction)
def delete_item(
    id: int,
    db: Session = Depends(get_db),
) -> Transaction:
    """
    Delete an asset balance.
    """
    return crud_transaction.remove(db=db, id=id)
