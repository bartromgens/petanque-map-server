from django.core.management.base import BaseCommand

from courts import overpass
from courts.models import Court


class Command(BaseCommand):
    help = 'Get all petanque courts'

    def handle(self, *args, **options):
        response_json = overpass.get_courts_utrecht(responseformat='json')
        # response_json = overpass.get_courts_nl(responseformat='json')
        # response_geojson = overpass.get_courts_utrecht(responseformat='geojson')
        # print(response_json)
        elements = response_json["elements"]
        court_properties = dict()
        for element in elements:
            # print(element)
            # print('type:', element['type'])
            # print('id:', element['id'])
            court_properties[element['id']] = {
                'osm_type': element['type']
            }
            if element['type'] == 'way':
                court_properties[element['id']]['lon'] = element['center']['lon']
                court_properties[element['id']]['lat'] = element['center']['lat']
            elif element['type'] == 'node':
                court_properties[element['id']]['lon'] = element['lon']
                court_properties[element['id']]['lat'] = element['lat']
        print('elements found:', len(elements))

        for osm_id, court in court_properties.items():
            print(court)
            Court.objects.update_or_create(
                osm_id=osm_id,
                defaults={
                    "osm_type": court['osm_type'],
                    "lon": court['lon'],
                    "lat": court['lat'],
                }
            )