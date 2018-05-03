from django.core.management.base import BaseCommand

from courts import overpass
from courts.models import Court


class Command(BaseCommand):
    help = 'Get all petanque courts'

    def handle(self, *args, **options):
        response_json = overpass.get_courts_utrecht(responseformat='json')
        response_geojson = overpass.get_courts_utrecht(responseformat='geojson')
        # print(response)
        elements = response_json["elements"]
        court_properties = dict()
        for element in elements:
            print(element)
            print('type:', element['type'])
            print('id:', element['id'])
            court_properties[element['id']] = {
                'osm_type': element['type']
            }
        print('elements found', len(elements))
        features = response_geojson["features"]
        for feature in response_geojson["features"]:
            court_property = court_properties[feature['id']]
            print(court_property)
            court_property['lon'] = feature['geometry']['coordinates'][0]
            court_property['lat'] = feature['geometry']['coordinates'][1]
            print(feature['geometry']['coordinates'])
        print('features found', len(features))

        for id, property in court_properties.items():
            print(property)
            Court.objects.filter(osm_id=id).delete()
            Court.objects.create(
                osm_id=id,
                osm_type=property['osm_type'],
                lon=property['lon'],
                lat=property['lat']
            )