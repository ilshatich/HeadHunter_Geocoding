from geocoders.geocoder import Geocoder
from api import API

# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:

        geo_data = API.get_area(area_id)
        address = geo_data.name

        while geo_data.parent_id:
            geo_data = API.get_area(geo_data.parent_id)
            address = f'{geo_data.name} {address}'

        return address


