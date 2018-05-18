from django.db import models


class Terrain(models.Model):
    osm_id = models.IntegerField(unique=True, null=False)
    osm_type = models.CharField(max_length=250, null=False, default='')
    lon = models.FloatField(null=False, default=0.0)
    lat = models.FloatField(null=False, default=0.0)

    @property
    def osm_url(self):
        return 'https://www.openstreetmap.org/' + str(self.osm_type) + '/' + str(self.osm_id)