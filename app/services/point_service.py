from app.db.entities.point import Point
from app.db.repositories.PointRepository import PointRepository
from app.schemas.point import PointCreateSchema
from app.validations.point_validations import validate_point_data
import pandas as pd



class PointService:
    def __init__(self, point_repository: PointRepository):
        self.point_repository = point_repository

    def create_point(self, basin: str, lat: float, long: float, climate: str):
        point = Point(basin=basin, lat=lat, long=long, climate=climate)
        validate_point_data(point)
        self.point_repository.add(point)
        return point

    def get_point(self, point_id: int):
        return self.point_repository.get(point_id)

    def get_points(self, skip: int = 0, limit: int = 10):
        return self.point_repository.list(skip, limit)
    def update_point(self, point_id: int, basin: str, lat: float, long: float, climate: str):
        point = Point(id=point_id, basin=basin, lat=lat, long=long, climate=climate)
        validate_point_data(point)
        return self.point_repository.update(point)

    def delete_point(self, point_id: int):
        return self.point_repository.delete(point_id)

    def import_points_from_csv(self, data: pd.DataFrame):
        for _, row in data.iterrows():
            print(data)
            self.create_point(
                basin=data.basin,
                lat=data.lat,
                long=data.long,
                climate=data.climate
            )

