from urllib.request import Request

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.db.repositories.PointRepository import PointRepository
from app.db.session import SessionLocal
from app.schemas.point import PointSchema, PointCreateSchema
from app.services.point_service import PointService
import pandas as pd
import io

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_point_service(db: Session = Depends(get_db)):
    point_repository = PointRepository(db)
    return PointService(point_repository)
@router.post("/", response_model=PointCreateSchema)
def create_point_api(point: PointCreateSchema, point_service: PointService = Depends(get_point_service)):
    try:
        return point_service.create_point(
            basin=point.basin,
            lat=point.lat,
            long=point.long,
            climate=point.climate
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=error)

@router.get("/{point_id}", response_model=PointSchema)
def read_point(point_id: int, point_service: PointService = Depends(get_point_service)):
    db_point = point_service.get_point(point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point

@router.get("/", response_model=list[PointSchema])
def read_points(skip: int = 0, limit: int = 10, point_service: PointService = Depends(get_point_service)):
    return point_service.get_points(skip=skip, limit=limit)

@router.put("/{point_id}", response_model=PointSchema)
def update_point_api(point_id: int, point: PointCreateSchema, point_service: PointService = Depends(get_point_service)):
    return point_service.update_point(
        point_id=point_id,
        basin=point.basin,
        lat=point.lat,
        long=point.long,
        climate=point.climate
    )

@router.delete("/{point_id}", response_model=PointSchema)
def delete_point_api(point_id: int, point_service: PointService = Depends(get_point_service)):
    return point_service.delete_point(point_id=point_id)

@router.post("/import-csv")
def import_points_csv(file: UploadFile = File(...), point_service: PointService = Depends(get_point_service)):
    try:
        contents = file.file.read().decode("utf-8")
        data = pd.read_csv(io.StringIO(contents))
        point_service.import_points_from_csv(data=data)
        return {"message": "CSV file imported successfully"}
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))

