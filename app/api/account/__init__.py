from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.account.crud import crud_account
from app.api.deps import get_db
from app.schemas.account import Account, AccountCreate, AccountUpdate

router = APIRouter()


@router.get("/{id}", response_model=Account)
def read_item(
    id: int,
    db: Session = Depends(get_db),
) -> Account:
    """
    Get account by ID.
    """
    return crud_account.get(db=db, id=id)


@router.get("/", response_model=List[Account])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Any:
    """
    Retrieve accounts.
    """
    return crud_account.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=Account)
def create_item(
    account_in: AccountCreate,
    db: Session = Depends(get_db),
) -> Account:
    """
    Create new account.
    """
    return crud_account.create(db=db, obj_in=account_in)


@router.put("/{id}", response_model=Account)
def update_item(
    id: int,
    account_in: AccountUpdate,
    db: Session = Depends(get_db),
) -> Account:
    """
    Update an account.
    """
    account = crud_account.get(db=db, id=id)
    return crud_account.update(db=db, db_obj=account, obj_in=account_in)


@router.delete("/{id}", response_model=Account)
def delete_item(
    id: int,
    db: Session = Depends(get_db),
) -> Account:
    """
    Delete an account.
    """
    return crud_account.remove(db=db, id=id)
