from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api import api_router

# from fastapi.staticfiles import StaticFiles
# from app.core import settings

BASE_PATH = Path(__file__).resolve().parent

app = FastAPI(title="My Ledger Book", openapi_url="/api/openapi.json")
# app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

app.include_router(api_router, prefix="/api")


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/docs")
