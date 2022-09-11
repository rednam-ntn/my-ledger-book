from fastapi import APIRouter

from app.api import account, asset, asset_balance, asset_price, asset_supplier, transaction

api_router = APIRouter()
api_router.include_router(account.router, prefix="/account", tags=["Account"])

api_router.include_router(asset.router, prefix="/asset", tags=["Asset"])
api_router.include_router(asset_balance.router, prefix="/asset/balance", tags=["Asset"])
api_router.include_router(asset_price.router, prefix="/asset/price", tags=["Asset"])
api_router.include_router(asset_supplier.router, prefix="/asset/supplier", tags=["Asset"])

api_router.include_router(transaction.router, prefix="/transaction", tags=["Transaction"])
