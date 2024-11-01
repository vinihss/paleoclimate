from sqlalchemy import Column, Float, Integer, String
from app.infrastructure.db.base import Base

class Point(Base):
    __tablename__ = 'points'

    id = Column(Integer, primary_key=True, autoincrement=True)
    basin = Column(String(200), nullable=False)
    lat = Column(Float(11), nullable=False)
    long = Column(Float(11), nullable=False)
    climate = Column(String(1), nullable=False)
    age = Column(Integer, nullable=False)
    lithology_weight = Column(Integer, nullable=True)
    paleontology_weight = Column(Integer, nullable=True)
    palinomorphs_weight = Column(Integer, nullable=True)
    geochemistry_weight = Column(Integer, nullable=True)
