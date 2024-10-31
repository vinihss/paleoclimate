# data_preprocessor.py
import pandas as pd

class DataPreprocessor:
    def __init__(self, climate_mapping: dict):
        self.climate_mapping = climate_mapping

    def preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
        data['climate'] = data['climate'].map(self.climate_mapping)
        return data.dropna(subset=['climate'])