from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api.account import router as account_router
from app.api.asset import router as asset_router

# from fastapi.staticfiles import StaticFiles
# from app.core import settings

BASE_PATH = Path(__file__).resolve().parent

app = FastAPI(title="Part Segment API", openapi_url="/openapi.json")
# app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

app.include_router(account_router)
app.include_router(asset_router)


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/docs")
