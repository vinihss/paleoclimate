from pydantic import BaseModel

class PointBase(BaseModel):
    lat: float
    long: float
    max_age: int
    min_age: int
    weight: float
    climate: str

class PointCreate(PointBase):
    pass

class Point(PointBase):
    id: int

    class Config:
        orm_mode = True