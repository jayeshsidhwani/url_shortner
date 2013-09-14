from django.http import HttpResponse, HttpResponseRedirect
import hashlib, time
from models import Urls


def home(request, code):
    url = Urls.objects.filter(code = code)
    return HttpResponseRedirect(url[0].long_url)

def create(request):
    url = request.GET.get('url')
    short_code = hashlib.sha1(url).hexdigest()[0:6]

    if Urls.objects.exists(code = short_code):
        return HttpResponse(short_code)
    else:
        new_url = Urls()
        new_url.code = short_code
        new_url.long_url = url
        new_url.created_at = int(time.time())
        new_url.save()
        return HttpResponse(short_code)