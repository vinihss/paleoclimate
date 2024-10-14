from app.schemas.point import PointCreateSchema

def validate_point_data(point: PointCreateSchema):
    if not point.basin or len(point.basin) > 200:
        raise ValueError("Bacia must be a non-empty string with a maximum length of 200 characters.")
    if not (-90 <= point.lat <= 90):
        raise ValueError("Latitude must be between -90 and 90 degrees.")
    if not (-180 <= point.long <= 180):
        raise ValueError("Longitude must be between -180 and 180 degrees.")
    if point.climate not in ('S', 'U', 'D'):
        raise ValueError("Paleoclima must be one of the predefined values: S, H, D")
