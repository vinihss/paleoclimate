from urllib.request import Request

from fastapi import APIRouter, Depends, HTTPException, File
from app.infrastructure.db.session import SessionLocal
from app.schemas.point import PointSchema, PointCreateSchema
from app.schemas.timescale import TimeScaleSchema
from app.domain.paleo_map.services import PaleoMapService
from pathlib import Path
import pandas as pd
import shutil

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_paleomap_service():
    return PaleoMapService()

@router.get("/{age}")
async def get_map(age: int, paleomap_service: PaleoMapService = Depends(get_paleomap_service)):
    return paleomap_service.get_map(age)


@router.get('/map')
async def generate_map():
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(**DB_CONFIG)

        # Carregar dados em um GeoDataFrame
        query = "SELECT latitude AS lat, longitude AS long, clima FROM sua_tabela"
        data = gpd.read_postgis(query, conn)

        # Converter para geometria
        data['geometry'] = gpd.points_from_xy(data['long'], data['lat'])

        # Criar um GeoDataFrame
        geo_data = gpd.GeoDataFrame(data, geometry='geometry')

        # Gerar um mapa (você pode usar Folium ou Matplotlib para isso)
        # Aqui está um exemplo com Folium
        import folium

        m = folium.Map(location=[data['lat'].mean(), data['long'].mean()], zoom_start=10)

        for _, row in geo_data.iterrows():
            folium.Marker([row['lat'], row['long']], popup=row['clima']).add_to(m)

        # Salvar o mapa em um arquivo HTML
        map_file = "mapa.html"
        m.save(map_file)

        return {"message": "Mapa gerado com sucesso", "map_file": map_file}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Fechar a conexão
        conn.close()
