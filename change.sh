#!/bin/bash

# Configurações do repositório
REPO_URL="https://github.com/vinihss/paleoclimate"
BRANCH_NAME="changePointEntity"
LOCAL_DIR="paleoclimate"
TOKEN=ghp_Wjl1SpZFGSXDRlvzIoZpqIPDo6sd160l1ZR


# Atualizar o arquivo models.py
echo "Atualizando models.py..."
cat <<EOL > models.py
from sqlalchemy import Column, Integer, String, Float, Base

class Point(Base):
    __tablename__ = 'points'

    id = Column(Integer, primary_key=True, autoincrement=True)
    basin = Column(String(200), nullable=False)
    lat = Column(Float(11), nullable=False)
    long = Column(Float(11), nullable=False)
    paleoclima = Column(String(1), nullable=False)
EOL

# Atualizar o arquivo database_setup.sql
echo "Atualizando database_setup.sql..."
cat <<EOL > database_setup.sql
CREATE TABLE points (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    basin VARCHAR(200) NOT NULL,
    lat FLOAT(11) NOT NULL,
    long FLOAT(11) NOT NULL,
    paleoclima CHAR(1) NOT NULL
);
EOL

# Atualizar o arquivo another_related_file.py
echo "Atualizando another_related_file.py..."
cat <<EOL > another_related_file.py
def insert_point(basin, lat, long, paleoclima):
    new_point = Point(
        basin=basin,
        lat=lat,
        long=long,
        paleoclima=paleoclima
    )
    session.add(new_point)
    session.commit()
EOL

# Adicionar e comitar as mudanças
echo "Adicionando e comitando mudanças..."
git add models.py database_setup.sql another_related_file.py
git commit -m "Atualizar entidade Point e suas classes relacionadas"

# Adicionar e comitar as mudanças
echo "Adicionando e comitando mudanças..."
git add models.py database_setup.sql another_related_file.py
git commit -m "Atualizar entidade Point e suas classes relacionadas"

git checkout -b $BRANCH_NAME

# Empurrar as mudanças para o repositório
echo "Empurrando mudanças para o repositório..."
git push origin $BRANCH_NAME
