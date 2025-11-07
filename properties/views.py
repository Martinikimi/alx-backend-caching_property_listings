from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all()
    data = {
        'properties': list(properties.values())
    }
    return JsonResponse({'data': data})
