from app.db.session import engine
from app.db.base import Base
from app.db.models.point import Point

def setup():
    Base.metadata.create_all(bind=engine)
    # Adicione aqui a importação de dados iniciais, se necessário

if __name__ == "__main__":
    setup()