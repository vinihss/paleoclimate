import geopandas as gpd
import os

def convert_shapefile_to_geojson(shapefile_path, geojson_path):
    base_name, _ = os.path.splitext(shapefile_path)
    required_extensions = ['.shp', '.shx', '.dbf', '.prj']
    missing_files = [base_name + ext for ext in required_extensions if not os.path.exists(base_name + ext)]

    if missing_files:
        raise FileNotFoundError(f"Os seguintes arquivos estão faltando: {', '.join(missing_files)}")

    gdf = gpd.read_file(shapefile_path)
    # Transformar para a projeção desejada, se necessário
    if gdf.crs != "EPSG:4326":
        gdf = gdf.to_crs("EPSG:4326")
    gdf.to_file(geojson_path, driver='GeoJSON')

# Exemplo de uso para múltiplos arquivos
shapefiles = {
    'coast': '/home/vini/Desktop/paleoclima-design/mapas-paleograficos-shape/65_coast.shp',
    'margin': '/home/vini/Desktop/paleoclima-design/mapas-paleograficos-shape/65_margin.shp'
}

for key, shapefile_path in shapefiles.items():
    geojson_path = f'./{key}.geojson'
    convert_shapefile_to_geojson(shapefile_path, geojson_path)
