import json

from cmsplugin_filer_image.models import ThumbnailOption
from django import http
from filer.models.imagemodels import Image


def url_image(request, image_id):
    image = Image.objects.get(pk=image_id)
    thumb_options = request.GET.get('thumb_options')
    width = request.GET.get('width')
    height = request.GET.get('height')

    url = image.url
    thumbnail_options = {}
    if thumb_options is not None:
        thumbnail_options = ThumbnailOption.objects.get(pk=thumb_options).as_dict
    
    if width and height:
        width = int(width)
        height = int(height)

        size = (width, height)
        thumbnail_options.update({'size': size})

    if thumbnail_options != {}:
        thumbnailer = image.easy_thumbnails_thumbnailer
        image = thumbnailer.get_thumbnail(thumbnail_options)
        url = image.url

    data = {
        'url': url,
        'width': image.width,
        'height': image.height,
    }
    return http.HttpResponse(json.dumps(data), content_type="application/json")


def thumbnail_options(request):
    response_data = [{'id': opt.pk, 'name': opt.name} for opt in ThumbnailOption.objects.all()]
    return http.HttpResponse(json.dumps(response_data), content_type="application/json")
