from fastapi import FastAPI
from app.presentation.api import point

app = FastAPI()

app.include_router(point.router, prefix="/points", tags=["points"])