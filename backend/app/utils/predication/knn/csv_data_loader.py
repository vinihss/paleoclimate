# csv_data_loader.py
import pandas as pd
from .data_loader import DataLoader

class CSVDataLoader(DataLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)