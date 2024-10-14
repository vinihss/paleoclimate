#!/bin/bash

# Inicializar Conda
eval "$(conda shell.bash hook)"

# Ativar ambiente Conda
conda activate paleoclimate

# Rodar Pylint
echo "Running pylint..."
pylint app/ || { echo 'Pylint failed' ; exit 1; }

# Rodar Flake8
echo "Running flake8..."
flake8 app/ || { echo 'Flake8 failed' ; exit 1; }

# Rodar Black
echo "Running black..."
black --check app/ || { echo 'Black failed' ; exit 1; }

# Rodar Autopep8
echo "Running autopep8..."
autopep8 --in-place --aggressive --aggressive --recursive app/

echo "All linters ran successfully."
