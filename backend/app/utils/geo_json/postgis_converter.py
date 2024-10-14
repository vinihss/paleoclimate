import psycopg2
import geopandas as gpd


class PostgisConverter:

    def __init__(self, conn):
        self.conn = conn

    def get_geojson(self, query):
        # Carregar dados em um GeoDataFrame
        data = gpd.read_postgis(query, self.conn)

        # Converter para geometria
        data['geometry'] = gpd.points_from_xy(data['long'], data['lat'])

        # Criar um GeoDataFrame
        geo_data = gpd.GeoDataFrame(data, geometry='geometry')
        return geo_data.to_json()