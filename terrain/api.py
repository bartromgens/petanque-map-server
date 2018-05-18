from rest_framework import serializers, viewsets

from terrain.models import Terrain


class TerrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Terrain
        fields = ('id', 'osm_id', 'osm_type', 'osm_url', 'lon', 'lat', 'url')


class TerrainViewSet(viewsets.ModelViewSet):
    queryset = Terrain.objects.all()
    serializer_class = TerrainSerializer
