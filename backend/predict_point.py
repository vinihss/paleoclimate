import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class WeightedKNN:
    """
    Implementa um KNN ponderado, considerando a confiabilidade do pesquisador
    (researcher_reliability) e a confiabilidade gerada pelo sistema (system_reliability).
    """
    def __init__(self, data_loader, k=5):
        self.data_loader = data_loader
        self.k = k
        self.model = KNeighborsClassifier(n_neighbors=k)
        self.train_model()

    def train_model(self):
        """
        Treina o modelo com os dados carregados.
        """
        features = self.data_loader.data[['lat', 'long', 'age']]
        labels = self.data_loader.data['climate']
        self.model.fit(features, labels)

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

class DataLoader:
    """
    Responsável por carregar e manter os dados coletados pelos pesquisadores.
    """
    def __init__(self, data_file):
        self.data = self.load_data(data_file)

    def load_data(self, file_path):
        """
        Carrega os dados de entrada de um arquivo CSV, contendo latitude, longitude,
        clima, confiabilidade geral, confiabilidade do sistema e idade.
        """
        import pandas as pd
        return pd.read_csv(file_path)


class ClimatePredictor:
    """
    Responsável por fazer predições de clima com base em lat, long e idade.
    """
    def __init__(self, data_loader):
        from sklearn.neighbors import KNeighborsClassifier
        self.data_loader = data_loader
        self.model = KNeighborsClassifier(n_neighbors=5)
        self.train_model()

    def train_model(self):
        """
        Treina o modelo com os dados carregados.
        """
        features = self.data_loader.data[['lat', 'long', 'age']]
        labels = self.data_loader.data['climate']
        self.model.fit(features, labels)

    def predict_climate(self, lat, long, age):
        """
        Prediz o clima para uma nova entrada de latitude, longitude e idade.
        """
        return self.model.predict([[lat, long, age]])

class ResearcherFeedback:
    """
    Responsável por gerenciar o feedback do pesquisador sobre a predição e a interpretação manual.
    """
    def __init__(self):
        self.feedback_data = []

    def give_feedback(self, lat, long, age, predicted_climate, interpreted_climate, reliability_score):
        """
        Recebe a interpretação do pesquisador, podendo ser diferente da predição original,
        além da avaliação de confiabilidade.
        """
        self.feedback_data.append({
            'lat': lat,
            'long': long,
            'age': age,
            'predicted_climate': predicted_climate,
            'interpreted_climate': interpreted_climate,  # Clima interpretado pelo pesquisador
            'reliability_score': reliability_score
        })

    def add_feedback_to_data(self, data_loader):
        """
        Adiciona os pontos interpretados como confiáveis ao conjunto de treinamento original.
        """
        for feedback in self.feedback_data:
            if feedback['reliability_score'] > 50:  # Exemplo: confiabilidade mínima para aceitar o ponto
                new_point = {
                    'lat': feedback['lat'],
                    'long': feedback['long'],
                    'age': feedback['age'],
                    'climate': feedback['interpreted_climate'],  # Usa o clima interpretado pelo pesquisador
                    'reliability': feedback['reliability_score']
                }
                data_loader.data = data_loader.data.append(new_point, ignore_index=True)

# Exemplo de fluxo de trabalho
data_loader = DataLoader('data.csv')  # Carrega os dados coletados
predictor = ClimatePredictor(data_loader)
feedback_manager = ResearcherFeedback()

# Exemplo de predição
lat, long, age = -13.83, -38.5, 120
predicted_climate = predictor.predict_climate(lat, long, age)

# Pesquisador avalia a predição e fornece uma interpretação manual
interpreted_climate = 'h'  # Clima ajustado manualmente pelo pesquisador
reliability_score = 75  # Pesquisador avalia a confiabilidade da predição

# O feedback é fornecido com a interpretação manual
feedback_manager.give_feedback(lat, long, age, predicted_climate, interpreted_climate, reliability_score)

# Atualiza o conjunto de dados com base no feedback
feedback_manager.add_feedback_to_data(data_loader)

# O modelo pode ser re-treinado com os novos dados adicionados
predictor.train_model()
