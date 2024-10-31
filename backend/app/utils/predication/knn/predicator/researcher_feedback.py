
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
