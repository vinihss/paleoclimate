import logging
from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from app.infrastructure.db.repositories.PointRepository import PointRepository
from app.infrastructure.db.session import SessionLocal
from app.schemas.point import PointSchema, PointCreateSchema
from app.domain.paleoclimate_evidence.services import PointService
import pandas as pd

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


@router.get("/{age_ini}/{age_end}")
async def read_points(age_ini: int, age_end: int, point_service: PointService = Depends(get_point_service)):
    """
        Return a collection of points by range of ages.
        Args:
            age_ini(int): The initial age of the points
            age_end (int): The final age of the points
        Returns:
            dict: A dictionary containing the points.
        """
    db_point = point_service.get_period(age_ini=age_ini, age_end=age_end)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point


@router.get("/", response_model=list[PointSchema])
async def read_points(skip: int = 0, limit: int = 10, point_service: PointService = Depends(get_point_service)):
    return point_service.get_points(skip=skip, limit=limit)


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
        raise HTTPException(status_code=422, detail=str(error))


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


@router.post("/import-xls")
async def import_points_csv(file: UploadFile = File(...), point_service: PointService = Depends(get_point_service)):
    logging.info("PRA ONDE VAI O MUNDO")
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    await point_service.import_points_by_xls_document(file=file)

    return {"message": "CSV file imported successfully"}


def read_point(point_id: int, point_service: PointService = Depends(get_point_service)):
    db_point = point_service.get_point(point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point
