
from django.conf.urls import url, include
from django.contrib import admin

from courts.api import CourtViewSet

from rest_framework import serializers, viewsets, routers

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'court', CourtViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
