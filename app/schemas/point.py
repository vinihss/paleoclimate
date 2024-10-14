
from pydantic import BaseModel, Field


class PointBaseSchema(BaseModel):
    basin: str
    lat: float
    long: float
    climate: str
    class Config:
        orm_mode = True
class PointCreateSchema(PointBaseSchema):
    pass

class PointSchema(PointBaseSchema):
    id: int
    class Config:
        orm_mode = True