from django.core.management.base import BaseCommand

from terrain import overpass


class Command(BaseCommand):
    help = 'Get overpass API status'

    def handle(self, *args, **options):
        response = overpass.get_api_status()
        print(response.text)
