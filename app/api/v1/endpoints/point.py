from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.point import Point, PointCreate
from app.services.point_service import create_point, delete_point, get_point, get_points, update_point

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Point)
def create_point_api(point: PointCreate, db: Session = Depends(get_db)):
    return create_point(db=db, point=point)

@router.get("/{point_id}", response_model=Point)
def read_point(point_id: int, db: Session = Depends(get_db)):
    db_point = get_point(db=db, point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return db_point

@router.get("/", response_model=list[Point])
def read_points(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_points(db=db, skip=skip, limit=limit)

@router.put("/{point_id}", response_model=Point)
def update_point_api(point_id: int, point: PointCreate, db: Session = Depends(get_db)):
    return update_point(db=db, point_id=point_id, point=point)

@router.delete("/{point_id}", response_model=Point)
def delete_point_api(point_id: int, db: Session = Depends(get_db)):
    return delete_point(db=db, point_id=point_id)