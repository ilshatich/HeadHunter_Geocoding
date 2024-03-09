from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

        self.__dict = {}

        for country in self.__data:
            for area in country.areas:
                for city in area.areas:
                    self.__dict[city.id] = f'{country.name} {area.name} {city.name}'
                self.__dict[area.id] = f'{country.name} {area.name}'
            self.__dict[country.id] = f'{country.name}'

    def _apply_geocoding(self, area_id: str) -> str:
        return self.__dict.get(area_id, "There is no such key in the dictionary")