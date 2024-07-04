from sqlalchemy.orm import Session
from app.db.entities.point import Point

class PointRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, point: Point):
        self.session.add(point)
        self.session.commit()
        return point


    def get(self, point_id: int):
        return self.session.query(Point).filter_by(id=point_id).first()

    def list(self, skip: int = 0, limit: int = 10):
        return self.session.query(Point).offset(skip).limit(limit).all()


    def update(self, point: Point):
        existing_point = self.get(point.id)
        if existing_point:
            existing_point.basin = point.bacia
            existing_point.lat = point.lat
            existing_point.long = point.long
            existing_point.climate = point.climate
            existing_point.age = point.age
            self.session.commit()
            return existing_point
        return None

    def delete(self, point_id: int):
        point = self.get(point_id)
        if point:
            self.session.delete(point)
            self.session.commit()
            return point
        return None
