from django.shortcuts import get_object_or_404

from rest_framework import serializers, viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from terrain.models import Terrain
from terrain.models import TerrainImage
from terrain.models import TerrainRating


class TerrainImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TerrainImage
        fields = ('id', 'terrain', 'file', 'url')


class TerrainImageViewSet(viewsets.ModelViewSet):
    queryset = TerrainImage.objects.all()
    serializer_class = TerrainImageSerializer


class TerrainRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerrainRating
        fields = ('id', 'terrain', 'rating', 'url')


class TerrainRatingViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = TerrainRating.objects.all()
    serializer_class = TerrainRatingSerializer


class TerrainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Terrain
        fields = ('id', 'osm_id', 'osm_type', 'osm_url', 'lon', 'lat', 'url')


class TerrainFullSerializer(serializers.HyperlinkedModelSerializer):
    images = TerrainImageSerializer(many=True, read_only=True)  # this works due to related name in model
    ratings = TerrainRatingSerializer(many=True, read_only=True)  # this works due to related name in model

    class Meta:
        model = Terrain
        fields = ('id', 'osm_id', 'osm_type', 'osm_url', 'lon', 'lat', 'url', 'images', 'ratings')


class TerrainViewSet(viewsets.ModelViewSet):
    queryset = Terrain.objects.all()
    serializer_class = TerrainSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Terrain.objects.all()
        terrain = get_object_or_404(queryset, pk=kwargs.get('pk'))
        serializer = TerrainFullSerializer(terrain, context={'request': request})
        return Response(serializer.data)


class TerrainImageView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (AllowAny,)

    def post(self, request, terrain_id, filename, *args, **kwargs):
        print(terrain_id, filename)
        terrain = Terrain.objects.get(id=terrain_id)
        print(request.data)
        terrain_image = TerrainImage.objects.create(terrain=terrain)
        file = request.data['file']
        terrain_image.file.save(filename, file, save=True)
        return Response(status=204)

