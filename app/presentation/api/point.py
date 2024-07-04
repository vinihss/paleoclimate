from urllib.request import Request

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.db.repositories.PointRepository import PointRepository
from app.db.session import SessionLocal
from app.schemas.point import PointSchema, PointCreateSchema
from app.schemas.timescale import TimeScaleSchema
from app.services.point_service import PointService
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

async def get_point_service(db: Session = Depends(get_db)):
    point_repository = PointRepository(db)
    return PointService(point_repository)
@router.post("/", response_model=PointCreateSchema)
async def create_point_api(point: PointCreateSchema, point_service: PointService = Depends(get_point_service)):
    try:
        return point_service.create_point(
            basin=point.basin,
            lat=point.lat,
            long=point.long,
            climate=point.climate,
            age=point.age
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=error)

@router.get("/{point_id}", response_model=PointSchema)
async def read_point(point_id: int, point_service: PointService = Depends(get_point_service)):
    db_point = point_service.get_point(point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point

@router.get("/", response_model=list[PointSchema])
async def read_points(skip: int = 0, limit: int = 10, point_service: PointService = Depends(get_point_service)):
    return point_service.get_points(skip=skip, limit=limit)

@router.put("/{point_id}", response_model=PointSchema)
async def update_point_api(point_id: int, point: PointCreateSchema, point_service: PointService = Depends(get_point_service)):
    return point_service.update_point(
        point_id=point_id,
        basin=point.basin,
        lat=point.lat,
        long=point.long,
        climate=point.climate
    )

@router.delete("/{point_id}", response_model=PointSchema)
async def delete_point_api(point_id: int, point_service: PointService = Depends(get_point_service)):
    return point_service.delete_point(point_id=point_id)


async def insert_points(point_service, df, sheet_name):
    for index, row in df.iterrows():
        point_service.create_point(
            basin=row['BACIA'],
            lat=row['LATITUDE'],
            long=row['LONGITUDE'],
            climate=row['PALEOCLIMA'],
            age=sheet_name
)


@router.post("/import-xls")
async def import_points_csv(file: UploadFile = File(...), point_service: PointService = Depends(get_point_service)):
    try:
        if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
            raise HTTPException(status_code=400, detail="Invalid file type")
        UPLOAD_DIR = Path("resources")

        file_location = UPLOAD_DIR / file.filename
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
            xls = pd.ExcelFile(file_location)
          # Percorrendo as abas a partir da segunda
            for sheet_name in xls.sheet_names[1:]:
                df = pd.read_excel(file_location, sheet_name=sheet_name)
                insert_points(point_service, df, sheet_name)
        return {"message": "CSV file imported successfully"}
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))



def read_point(point_id: int, point_service: PointService = Depends(get_point_service)):
    db_point = point_service.get_point(point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point

