
from pathlib import Path



class PaleoMapService:
    def __init__(self):
        return

    def get_map(self, age: int):
        map_file = f'app/geojson_layers/{age}.json'
        path = Path(map_file)
        return path.read_text()
