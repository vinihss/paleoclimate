import psycopg2
import geopandas as gpd
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import numpy as np

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname='seu_banco_de_dados',
    user='seu_usuario',
    password='sua_senha',
    host='localhost',  # ou o endereço do seu servidor
    port='5432'  # padrão do PostgreSQL
)

# Carregar dados em um GeoDataFrame
query = "SELECT latitude AS lat, longitude AS long, clima FROM sua_tabela"
data = gpd.read_postgis(query, conn)

# Extrair coordenadas e valores
latitudes = data['lat']
longitudes = data['long']
valores = data['clima']  # Coluna que você quer interpolar

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

# Fechar a conexão
conn.close()
