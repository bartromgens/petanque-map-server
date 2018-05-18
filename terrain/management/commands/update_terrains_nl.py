from django.core.management.base import BaseCommand

from terrain import factory
from terrain import overpass


class Command(BaseCommand):
    help = 'Get all petanque terrains in the Netherlands'

    def handle(self, *args, **options):
        # response_geojson = overpass.get_terrains_nl(responseformat='geojson')
        response_json = overpass.get_terrains_nl(responseformat='json')
        factory.create_terrains_from_overpass(response_json)
