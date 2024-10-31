# sgbd_data_loader.py
import pandas as pd
from data_loader import DataLoader
import sqlalchemy

class SGBDDataLoader(DataLoader):
    def __init__(self, connection_string: str, query: str):
        self.connection_string = connection_string
        self.query = query

    def load_data(self) -> pd.DataFrame:
        engine = sqlalchemy.create_engine(self.connection_string)
        return pd.read_sql_query(self.query, engine)