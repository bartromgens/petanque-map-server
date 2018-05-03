from django.core.management.base import BaseCommand

from courts import overpass


class Command(BaseCommand):
    help = 'Kill my running overpass queries'

    def handle(self, *args, **options):
        response = overpass.kill_my_queries()
        print(response.text)
