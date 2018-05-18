from django.core.management.base import BaseCommand

from terrain import factory
from terrain import overpass


class Command(BaseCommand):
    help = 'Get all petanque terrains in Utrecht'

    def handle(self, *args, **options):
        # response_geojson = overpass.get_terrains_utrecht(responseformat='geojson')
        response_json = overpass.get_terrains_utrecht(responseformat='json')
        factory.create_terrains_from_overpass(response_json)