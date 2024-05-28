from fastapi import FastAPI
from app.api.v1.endpoints import point

app = FastAPI()

app.include_router(point.router, prefix="/points", tags=["points"])