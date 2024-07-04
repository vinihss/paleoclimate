from app.db.session import engine
from app.db.base import Base
from app.db.entities.point import Point
from app.db.repositories.PointRepository import PointRepository as Repository
import pandas as pd

# Inserindo os dados no banco de dados
def insert_points(repository:Repository, df):
    for index, row in df.iterrows():
        point = Point(
            id=row['ID'],
            basin=row['BACIA'],
            lat=row['LATITUDE'],
            long=row['LONGITUDE'],
            climate=row['PALEOCLIMA']
            climate=row['PALEOCLIMA']
        )
        repository.add(point)
def import_points():
    Base.metadata.create_all(bind=engine)
    file_path = 'tabela_idades_final.xls'
    xls = pd.ExcelFile(file_path)
    for sheet_name in xls.sheet_names[1:]:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        insert_points(Repository, df)


def setup():

    import_points()
    # Adicione aqui a importação de dados iniciais, se necessário

if __name__ == "__main__":
    setup()