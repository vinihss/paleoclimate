from sqlalchemy.orm import Session
from app.db.models.point import Point
from app.schemas.point import PointCreate
import pandas as pd

def get_point(db: Session, point_id: int):
    return db.query(Point).filter(Point.id == point_id).first()

def get_points(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Point).offset(skip).limit(limit).all()

def create_point(db: Session, point: PointCreate):
    db_point = Point(**point.dict())
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

def update_point(db: Session, point_id: int, point: PointCreate):
    db_point = db.query(Point).filter(Point.id == point_id).first()
    for key, value in point.dict().items():
        setattr(db_point, key, value)
    db.commit()
    db.refresh(db_point)
    return db_point

def delete_point(db: Session, point_id: int):
    db_point = db.query(Point).filter(Point.id == point_id).first()
    db.delete(db_point)
    db.commit()
    return db_point

def import_points_from_csv(db: Session, data: pd.DataFrame):
    for _, row in data.iterrows():
        point = Point(
            lat=row['lat'],
            long=row['long'],
            max_age=row['max_age'],
            min_age=row['min_age'],
            weight=row['weight'],
            climate=row['climate']
        )
        db.add(point)
    db.commit()