import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class ClimatePredictor:
    """
    Responsável por fazer predições de clima com base em lat, long e idade.
    """
    def __init__(self, data_loader):
        from sklearn.neighbors import KNeighborsClassifier
        self.data_loader = data_loader
        self.model = KNeighborsClassifier(n_neighbors=5)
        self.train_model()



    def predict_climate(self, lat, long, age):
        return self.model.predict([[lat, long, age]])
