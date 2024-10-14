import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

class DataLoader:
    """
    Classe responsável por carregar os dados de pesquisa geológica.
    """
    def __init__(self, data_source=None):
        self.data_source = data_source
        self.data = None

    def load_data(self):
        """
        Método para carregar dados de uma fonte (aqui simulamos com um DataFrame).
        """
        if self.data_source is None:
            self.data = pd.DataFrame({
                'lat': [-13.83, -10.5, -15.0, -20.0],
                'long': [-38.5, -40.0, -37.0, -42.0],
                'age': [145, 130, 120, 140],
                'confiabilidade': [2, 4, 3, 5],
                'climate': ['h', 's', 'h', 't']  # h = hot, s = semiarid, t = tropical
            })
        else:
            # Carregar dados de outra fonte, como CSV ou banco de dados
            pass
        return self.data

class Preprocessor:
    """
    Classe responsável por normalizar os dados e prepará-los para o modelo.
    """
    def __init__(self):
        self.scaler = StandardScaler()

    def preprocess_data(self, data):
        """
        Normaliza os dados de latitude, longitude e idade, ignorando a confiabilidade.
        """
        X = data[['lat', 'long', 'age']]
        y = data['climate']
        X_scaled = self.scaler.fit_transform(X)
        return X_scaled, y

    def preprocess_single_point(self, point):
        """
        Normaliza um ponto único para predição.
        """
        return self.scaler.transform(point)

class ClimateModel:
    """
    Classe responsável pelo treinamento e gerenciamento do modelo KNN.
    """
    def __init__(self, n_neighbors=3):
        self.model = KNeighborsClassifier(n_neighbors=n_neighbors)

    def train(self, X, y):
        """
        Treina o modelo KNN com os dados normalizados.
        """
        self.model.fit(X, y)

    def predict(self, point):
        """
        Prediz o clima para um ponto hipotético.
        """
        return self.model.predict(point)

class Predictor:
    """
    Classe responsável por orquestrar a predição de clima para um novo ponto.
    """
    def __init__(self, model, preprocessor):
        self.model = model
        self.preprocessor = preprocessor

    def predict_climate(self, lat, long, age):
        """
        Faz a predição do clima com base na latitude, longitude e idade.
        """
        ponto_hipotetico = pd.DataFrame({
            'lat': [lat],
            'long': [long],
            'age': [age]
        })

        # Pré-processar o ponto
        ponto_hipotetico_scaled = self.preprocessor.preprocess_single_point(ponto_hipotetico)

        # Fazer a previsão
        return self.model.predict(ponto_hipotetico_scaled)[0]

# Orquestração
def main():
    # Carregar os dados
    data_loader = DataLoader()
    data = data_loader.load_data()

    # Preprocessar os dados
    preprocessor = Preprocessor()
    X_scaled, y = preprocessor.preprocess_data(data)

    # Treinar o modelo
    climate_model = ClimateModel(n_neighbors=3)
    climate_model.train(X_scaled, y)

    # Instanciar o preditor
    predictor = Predictor(climate_model, preprocessor)

    # Exemplo de uso: prever clima para lat=-16, long=-39, idade=135
    lat_hipotetica = -16
    long_hipotetica = -39
    idade_hipotetica = 135
    previsao_clima = predictor.predict_climate(lat_hipotetica, long_hipotetica, idade_hipotetica)

    print(f'O clima previsto para a posição ({lat_hipotetica}, {long_hipotetica}) e idade {idade_hipotetica} é: {previsao_clima}')

if __name__ == "__main__":
    main()
