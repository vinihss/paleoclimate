from app.infrastructure.db.entities.point import Point
from app.infrastructure.db.repositories.PointRepository import PointRepository
from app.validations.point_validations import validate_point_data
import pandas as pd
import logging
import diskcache as dc
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


logger = logging.getLogger(__name__)

class PointService:
    def __init__(self, point_repository: PointRepository):
        self.point_repository = point_repository

    def create_point(self, basin: str, lat: float, long: float, climate: str, age: int):
        point = Point(basin=basin, lat=lat, long=long, climate=climate, age=age)
       # validate_point_data(point)
        self.point_repository.add(point)
        return point

    def get_point(self, point_id: int):
        return self.point_repository.get(point_id)

    def get_period(self, age_ini: int, age_end: int):
        return self.point_repository.get_period(age_ini, age_end)

    def get_points(self, skip: int = 0, limit: int = 10):
        return self.point_repository.list(skip, limit)
    def update_point(self, point_id: int, basin: str, lat: float, long: float, climate: str, age: int):
        point = Point(id=point_id, basin=basin, lat=lat, long=long, climate=climate, age=point.age)
        validate_point_data(point)
        return self.point_repository.update(point)

    def delete_point(self, point_id: int):
        return self.point_repository.delete(point_id)

    async def import_points_by_xls_document(self, file):
        # Lendo o arquivo diretamente da memória
        contents =  await file.read()
        logger.debug(contents)
        xls = pd.ExcelFile(contents)



        # Percorrendo as abas a partir da segunda
        for sheet_name in xls.sheet_names[1:]:
            df = pd.read_excel(xls, sheet_name=sheet_name)


            for index, row in df.iterrows():
                try:
                    if pd.isnull(row['BACIA']) or pd.isnull(row['LATITUDE']) or pd.isnull(row['LONGITUDE']) or pd.isnull(row['PALEOCLIMA']):
                        raise ValueError(f"Missing data in sheet {sheet_name}, row {index}")

                    self.create_point(
                        basin=row['BACIA'],
                        lat=row['LATITUDE'],
                        long=row['LONGITUDE'],
                        climate=row['PALEOCLIMA'],
                        age=sheet_name
                    )
                except ValueError as error:
                    logging.warning(error)
