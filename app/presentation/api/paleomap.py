from urllib.request import Request

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.db.repositories.PointRepository import PointRepository
from app.db.session import SessionLocal
from app.schemas.point import PointSchema, PointCreateSchema
from app.schemas.timescale import TimeScaleSchema
from app.services.paleomap_service import PaleoMapService
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

def get_paleomap_service():
    return PaleoMapService()

@router.get("/{age}")
async def get_map(age: int, paleomap_service: PaleoMapService = Depends(get_paleomap_service)):
    return paleomap_service.get_map(age)

