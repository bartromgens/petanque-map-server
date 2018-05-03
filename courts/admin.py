from django.contrib import admin

from courts.models import Court

class CourtAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'osm_id',
        'osm_type',
        'osm_url',
        'lon',
        'lat',
    )

admin.site.register(Court, CourtAdmin)
