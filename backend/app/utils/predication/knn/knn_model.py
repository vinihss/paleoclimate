# knn_model.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import logging

class KNNModel:
    def __init__(self, n_neighbors=3):
        self.models_by_age = {}
        self.scalers_by_age = {}
        self.n_neighbors = n_neighbors

    def train(self, data: pd.DataFrame):
        try:
            unique_ages = data['age'].unique()
            for age in unique_ages:
                age_data = data[data['age'] == age]
                features = age_data[['lat', 'long', 'paleontology_weight', 'lithology_weight', 'palynomorphs_weight', 'geochemistry_weight']]
                target = age_data['climate']

                scaler = StandardScaler()
                features_scaled = scaler.fit_transform(features)

                knn = KNeighborsClassifier(n_neighbors=self.n_neighbors)
                knn.fit(features_scaled, target)

                self.models_by_age[age] = knn
                self.scalers_by_age[age] = scaler
            logging.info('Model training completed successfully.')
        except Exception as e:
            logging.error(f'Error during training: {e}')

    def predict(self, lat, lon, paleontology_weight, lithology_weight, palynomorphs_weight, geochemistry_weight, age):
        try:
            if age not in self.models_by_age:
                logging.error(self.models_by_age)

                raise ValueError(f'No trained model found for age: {age}')

            scaler = self.scalers_by_age[age]
            features = pd.DataFrame([[lat, lon, paleontology_weight, lithology_weight, palynomorphs_weight, geochemistry_weight]],
                                    columns=['lat', 'long', 'paleontology_weight', 'lithology_weight', 'palynomorphs_weight', 'geochemistry_weight'])
            features_scaled = scaler.transform(features)

            knn = self.models_by_age[age]
            prediction = knn.predict(features_scaled)
            return prediction[0]
        except Exception as e:
            logging.error(f'Error during prediction: {e}')
            return None