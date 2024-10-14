import logging
from urllib.request import Request
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from app.infrastructure.db.repositories.PointRepository import PointRepository
from app.infrastructure.db.session import SessionLocal
from app.schemas.point import PointSchema, PointCreateSchema
from app.domain.paleoclimate_evidence.services import PointService
import pandas as pd

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




async def get_point_service(db: Session = Depends(get_db)):
    point_repository = PointRepository(db)
    return PointService(point_repository)

@router.post('/predict')
async def predict(point: PointCreateSchema, point_service: PointService = Depends(get_point_service)):
    try:
        return point_service.create_point(
            basin=point.basin,
            lat=point.lat,
            long=point.long,
            climate=point.climate,
            age=point.age
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))
    try:


        # Inserir o ponto e a predição no banco de dados
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO sua_tabela (latitude, longitude, clima, idade) VALUES (%s, %s, %s, %s)",
                (point.lat, point.long, clima_predito, point.idade)
            )
            conn.commit()

        return {"message": "Predição criada com sucesso", "clima": clima_predito}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Fechar a conexão
        conn.close()
