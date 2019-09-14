
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from terrain.api import TerrainViewSet
from terrain.api import TerrainImageViewSet
from terrain.api import TerrainImageView
from terrain.api import TerrainRatingViewSet
from terrain.views import get_terrain_image_thumbnail_url

from rest_framework import serializers, viewsets, routers

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'terrain/images', TerrainImageViewSet)
router.register(r'terrain/rating', TerrainRatingViewSet)
router.register(r'terrain', TerrainViewSet)

urlpatterns = [
    url(r'^v1/terrain/image/(?P<image_id>[^/.]+)/(?P<size>[^/.]+)', view=get_terrain_image_thumbnail_url),
    url(r'^v1/terrain/(?P<terrain_id>[^/.]+)/image/upload/(?P<filename>[^/]+)$', TerrainImageView.as_view()),
    url(r'^v1/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
