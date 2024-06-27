#!/bin/bash

# Diretório raiz do projeto
PROJECT_DIR="$(pwd)"

# Configurar e ativar ambiente virtual, se necessário
if [ -d "venv" ]; then
    echo "Ativando ambiente virtual..."
    source venv/bin/activate
fi

# Instalar as ferramentas, se não estiverem instaladas
echo "Instalando ferramentas de qualidade de código..."
pip install pylint flake8 black autopep8

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
