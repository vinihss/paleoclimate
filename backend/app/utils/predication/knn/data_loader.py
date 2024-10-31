# data_loader.py
from abc import ABC, abstractmethod
import pandas as pd

class DataLoader(ABC):
    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        pass