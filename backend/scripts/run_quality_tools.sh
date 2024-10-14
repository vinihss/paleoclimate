#!/bin/bash

# Diretório raiz do projeto
PROJECT_DIR="$APPLICATION_PATH"

source activate paleoclimate


# Executar pylint
echo "Executando pylint..."
find $PROJECT_DIR -type f -name "*.py" | xargs pylint

# Executar flake8
echo "Executando flake8..."
flake8 $PROJECT_DIR

# Executar black
echo "Executando black..."
black $PROJECT_DIR

# Executar autopep8
echo "Executando autopep8..."
autopep8 --in-place --aggressive --aggressive --recursive $PROJECT_DIR

echo "Ferramentas de qualidade de código executadas com sucesso."
