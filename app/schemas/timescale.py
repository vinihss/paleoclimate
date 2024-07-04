from pydantic import BaseModel, Field

class TimeScaleSchema(BaseModel):
    name: str
    year: int
    class Config:
        orm_mode = True
