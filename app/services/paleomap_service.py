from pathlib import Path



class PaleoMapService:
    def __init__(self):
        return

    def get_map(self, age: int):
        map_file = f',app/peleomaps/65_coast_converted.geojson'
        path = Path(map_file)
        return path.read_text()