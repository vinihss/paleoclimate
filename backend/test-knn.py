import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import numpy as np

# Definir o caminho do arquivo CSV
csv_file_path = 'dados_clima.csv'  # Substitua pelo caminho real do arquivo CSV

# Carregar os dados do CSV em um DataFrame
df = pd.read_csv(csv_file_path)

# Criar a geometria a partir de lat e long
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['long'], df['lat']))

# Definir o CRS (Sistema de Referência de Coordenadas), por exemplo, WGS84 (EPSG:4326)
gdf.set_crs(epsg=4326, inplace=True)

# Mapeamento de climas (ajuste conforme os dados do seu CSV)
climate_mapping = {
    'h': 1,  # Exemplo: "h" para 1
    'm': 2,  # Exemplo: "m" para 2
    'l': 3   # Exemplo: "l" para 3
    # Adicione outros mapeamentos conforme necessário
}
gdf['climate'] = gdf['climate'].map(climate_mapping)

# Extrair coordenadas e valores
latitudes = gdf['lat']
longitudes = gdf['long']
valores = gdf['climate']  # Agora deve ser numérico

# Criar uma grade para interpolação
grid_lat, grid_lon = np.mgrid[min(latitudes):max(latitudes):100j,
                     min(longitudes):max(longitudes):100j]
grid_values = griddata((latitudes, longitudes), valores,
                       (grid_lon, grid_lat), method='cubic')

# Plotar o mapa
plt.imshow(grid_values.T, extent=(min(longitudes), max(longitudes),
                                  min(latitudes), max(latitudes)), origin='lower')
plt.scatter(longitudes, latitudes, c='red')  # Ponto original
plt.colorbar(label='Clima')
plt.title('Interpolação de Clima')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
