from django.core.management.base import BaseCommand, CommandError

from courts import overpass


class Command(BaseCommand):
    help = 'Get all petanque courts'

    def handle(self, *args, **options):
        response = overpass.get_country_area_id()
        features = response["features"]
        for feature in response["features"]:
            print(feature['properties'])
        print('features found', len(features))