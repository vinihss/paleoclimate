import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Exemplo de dados (substitua por seus dados reais)
dados = [
    {"bacia": "camamu-almada", "latitude": -13.83, "longitude": -38.5, "paleoclima": "h"},
    {"bacia": "araripe", "latitude": -7.50, "longitude": -39.5, "paleoclima": "h"},
    # Adicione mais pontos aqui
]

# Criando uma GeoDataFrame a partir dos dados
geometry = [Point(d["longitude"], d["latitude"]) for d in dados]
gdf = gpd.GeoDataFrame(dados, geometry=geometry)

# Plotando os pontos
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Criando o plot
fig, ax = plt.subplots(figsize=(10, 10))
world.plot(ax=ax, color='lightgray')
gdf.plot(ax=ax, color='red', marker='o', markersize=50, label='Pontos de Paleoclima')

# Adicionando detalhes ao mapa
plt.title('Visualização dos Pontos de Paleoclima')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()
