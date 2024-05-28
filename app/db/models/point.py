from sqlalchemy import Column, Float, Integer, String
from app.db.base import Base

class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    max_age = Column(Integer, nullable=False)
    min_age = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    climate = Column(String, nullable=False)