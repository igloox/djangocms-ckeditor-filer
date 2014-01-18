from django.http import HttpResponseNotFound
from views import thumbnail_options, url_image


class ThumbnailMiddleware:
	def process_request(self, request):
		if "djangocms_ckeditor_filer_thumbnail_options" in request.GET:
			return thumbnail_options(request)
		
		if request.GET.get('djangocms_ckeditor_filer_image'):
			return url_image(request, request.GET.get('djangocms_ckeditor_filer_image'))
		
		# if the key is set but doesn't have a value (i.e., if the javascript is
		# being weird, just 404
		if request.GET.has_key('djangocms_ckeditor_filer_image'):
			return HttpResponseNotFound()
