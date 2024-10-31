
from pydantic import BaseModel, Field


class PointBaseSchema(BaseModel):
    basin: str
    lat: float
    long: float
    climate: str
    age: int
    lithology_weight: int
    paleontology_weight: int
    palynomorphs_weight: int
    geochemistry_weight: int
    class Config:
        orm_mode = True
class PointCreateSchema(PointBaseSchema):
    pass

class PointCreateSchema(PointBaseSchema):
    pass

class PointSchema(PointBaseSchema):
    id: int
    class Config:
        orm_mode = True