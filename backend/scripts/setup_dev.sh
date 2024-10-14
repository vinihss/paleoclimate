#!/bin/bash
# Script para configurar o ambiente de desenvolvimento

# Inicializar Conda
eval "$(conda shell.bash hook)"

# Criar e ativar o ambiente Conda (se ainda não criado)
if conda info --envs | grep -q 'paleoclimate'; then
    echo "Activating existing conda environment 'paleoclimate'"
    conda activate paleoclimate
else
    echo "Creating and activating new conda environment 'paleoclimate'"
    conda env create -f environment.yml
    conda activate paleoclimate
fi

# Executar migrações
alembic upgrade head

# Importar dados iniciais
python app/scripts/data_import/import_initial_data.py

# Executar linters
./scripts/run_lints.sh

# Iniciar servidor de desenvolvimento
./scripts/start.sh
