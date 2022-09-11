# from typing import List

# from fastapi.encoders import jsonable_encoder
# from sqlalchemy.orm import Session

from app.db.crud_base import CRUD
from app.db.models.asset_balance import AssetBalance
from app.schemas.asset_balance import AssetBalanceCreate, AssetBalanceUpdate


class CRUDAssetBalance(CRUD[AssetBalance, AssetBalanceCreate, AssetBalanceUpdate]):
    ...
    # TODO
    # def create_with_owner(self, db: Session, *, obj_in: AssetCreate) -> Asset:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data)

    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    # def get_multi_by_supplier(
    #     self, db: Session, *, asset_supplier_id: int, skip: int = 0, limit: int = 100
    # ) -> List[Asset]:
    #     return db.query(self.model).filter(Asset.asset_supplier_id == asset_supplier_id).offset(skip).limit(limit).all()


crud_asset_balance = CRUDAssetBalance(AssetBalance)
