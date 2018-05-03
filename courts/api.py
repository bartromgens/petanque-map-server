from rest_framework import serializers, viewsets

from courts.models import Court


class CourtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Court
        fields = ('id', 'osm_id', 'osm_type', 'osm_url', 'lon', 'lat', 'url')


class CourtViewSet(viewsets.ModelViewSet):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
