from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.presentation.api import point, timescale, paleomap
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()
# Configurar as origens permitidas
# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(point.router, prefix="/points", tags=["points"])
app.include_router(timescale.router, prefix="/timescale", tags=["timescale"])
app.include_router(paleomap.router, prefix="/paleomap", tags=["pa"
                                                              ""
                                                              ""
                                                              ""
                                                              ""
                                                              "leomap"]






