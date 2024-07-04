from urllib.request import Request

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.db.repositories.PointRepository import PointRepository
from app.db.session import SessionLocal
from app.schemas.point import PointSchema, PointCreateSchema
from app.schemas.timescale import TimeScaleSchema
from app.services.timescale_service import TimeScaleService
from pathlib import Path
import pandas as pd
import shutil

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_timescale_service():
    return TimeScaleService()

@router.get("/")
async def  get_time_scale(skip: int = 0, limit: int = 10, timescale_service: TimeScaleService = Depends(get_timescale_service)):
    return timescale_service.get_timescale(skip=skip, limit=limit)

