#!/bin/bash
# Script para configurar o ambiente de produção

# Criar e ativar o ambiente Conda
conda env create -f environment.yml
source activate paleoclimate

# Executar migrações
alembic upgrade head

# Iniciar servidor de produção
./scripts/start.sh
