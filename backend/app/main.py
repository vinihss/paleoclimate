from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.presentation.api import point, timescale, paleomap, predict

import os
import logging
import sys


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)




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
app.include_router(paleomap.router, prefix="/paleomap", tags=["paleomap"])
app.include_router(predict.router, prefix="/paleo-insights", tags=["PaleoInsights"])






