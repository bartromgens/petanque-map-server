from easy_thumbnails.files import get_thumbnailer
from django.http import JsonResponse

from terrain.models import TerrainImage


def get_terrain_image_thumbnail_url(request, image_id, size):
    options = {'size': (size, size), 'crop': False}
    image = TerrainImage.objects.get(id=image_id)
    thumb_url = get_thumbnailer(image.file).get_thumbnail(options).url
    return JsonResponse({'url': thumb_url})

