from django.core.management.base import BaseCommand

from terrain import overpass


class Command(BaseCommand):
    help = 'Get overpass API status'

    def handle(self, *args, **options):
        response = overpass.get_country_area_id()
        print(response['elements'][0]['id'])
