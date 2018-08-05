from django.core.management.base import BaseCommand

from terrain import factory
from terrain import overpass


class Command(BaseCommand):
    help = 'Get all petanque terrains in the world'

    def handle(self, *args, **options):
        responses = overpass.get_terrains_world(responseformat='json')
        for response_json in responses:
            factory.create_terrains_from_overpass(response_json)
