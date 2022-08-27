from fastapi import APIRouter

from app.api import account, asset

api_router = APIRouter()
api_router.include_router(asset.router, prefix="/asset", tags=["asset"])
api_router.include_router(account.router, prefix="/account", tags=["account"])
