from django.contrib import admin

from terrain.models import Terrain
from terrain.models import TerrainImage
from terrain.models import TerrainRating


class TerrainAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'osm_id',
        'osm_type',
        'osm_url',
        'lon',
        'lat',
    )


class TerrainImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'terrain',
        'file',
    )


class TerrainRatingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'terrain',
        'rating',
    )


admin.site.register(Terrain, TerrainAdmin)
admin.site.register(TerrainImage, TerrainImageAdmin)
admin.site.register(TerrainRating, TerrainRatingAdmin)
