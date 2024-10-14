import diskcache as dc
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from app.core.config import settings

from backend.knn1 import DataLoader


class Trainer:
    """
    Implementa um KNN ponderado, considerando a confiabilidade do pesquisador
    (researcher_reliability) e a confiabilidade gerada pelo sistema (system_reliability).
    """
    def __init__(self,  data_loader: DataLoader, k=5):
        self.data_loader = data_loader
        self.k = k
        self.model = KNeighborsClassifier(n_neighbors=k)
        self.cache =  settings.CACHE

    def train_model(self, force_retrain=False):
        cache_key = f'knn_model_paleoclimate'  # Chave única para o cache

            # Verifica se o modelo já foi treinado e está no cache
        if cache_key in  self.cache and not force_retrain:
            print("Modelo carregado do cache.")
            knn =  self.cache[cache_key]
        else:

            features = self.data_loader.data[['lat', 'long', 'age']]
            labels = self.data_loader.data['climate']

            self.model.fit(features, labels)

            # Armazena o modelo treinado no cache
            settings.CACHE[cache_key] = self.model
            print("Modelo treinado e armazenado no cache.")

        return knn




    def weighted_knn(self, lat, long, age):
        """
        Prediz o clima com base no KNN ponderado pela confiabilidade (priorizando a do pesquisador).
        """
        distances, indices = self.model.kneighbors([[lat, long, age]], self.k, return_distance=True)

        # Recuperar as confiabilidades (primeiro tenta a do pesquisador, depois a do sistema)
        neighbors = self.data_loader.data.iloc[indices[0]]
        neighbors_reliability = np.where(neighbors['researcher_reliability'].notnull(),
                                         neighbors['researcher_reliability'],
                                         neighbors['system_reliability'])
        neighbors_climate = neighbors['climate']

        # Calcula os pesos com base na confiabilidade (valores entre 0 e 1)
        weights = np.array(neighbors_reliability) / 100  # Converte para proporção

        # Contabiliza o clima com base nos pesos
        weighted_climates = {}
        for i, climate in enumerate(neighbors_climate):
            if climate in weighted_climates:
                weighted_climates[climate] += weights[i]
            else:
                weighted_climates[climate] = weights[i]

        # Retorna o clima com o maior peso total
        return max(weighted_climates, key=weighted_climates.get)

