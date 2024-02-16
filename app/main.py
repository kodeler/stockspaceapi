# app/main.py

from fastapi import FastAPI
from app.core import config
from app.api.api_router import router as api_router

app = FastAPI()

app.include_router(api_router)

