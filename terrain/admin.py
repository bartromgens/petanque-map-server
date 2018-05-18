from django.contrib import admin

from terrain.models import Terrain

class TerrainAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'osm_id',
        'osm_type',
        'osm_url',
        'lon',
        'lat',
    )

admin.site.register(Terrain, TerrainAdmin)
