from django.core.management.base import BaseCommand

from terrain import overpass
from terrain.models import Terrain


class Command(BaseCommand):
    help = 'Get all petanque terrain'

    def handle(self, *args, **options):
        response_json = overpass.get_terrains_utrecht(responseformat='json')
        # response_json = overpass.get_terrains_nl(responseformat='json')
        # response_geojson = overpass.get_terrains_utrecht(responseformat='geojson')
        # print(response_json)
        elements = response_json["elements"]
        terrain_properties = dict()
        for element in elements:
            # print(element)
            # print('type:', element['type'])
            # print('id:', element['id'])
            terrain_properties[element['id']] = {
                'osm_type': element['type']
            }
            if element['type'] == 'way':
                terrain_properties[element['id']]['lon'] = element['center']['lon']
                terrain_properties[element['id']]['lat'] = element['center']['lat']
            elif element['type'] == 'node':
                terrain_properties[element['id']]['lon'] = element['lon']
                terrain_properties[element['id']]['lat'] = element['lat']
        print('elements found:', len(elements))

        for osm_id, terrain in terrain_properties.items():
            print(terrain)
            Terrain.objects.update_or_create(
                osm_id=osm_id,
                defaults={
                    "osm_type": terrain['osm_type'],
                    "lon": terrain['lon'],
                    "lat": terrain['lat'],
                }
            )