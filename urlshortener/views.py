from django.http import HttpResponse, HttpResponseRedirect
import hashlib, time
from store import Urls
import ast
from config import SHORT_URL_HOST


def home(request, code):
    store_object = Urls()
    url_object = store_object.fetch(code)

    if code is None or url_object is None:
        return HttpResponseRedirect('/')
    else:
        url_object = ast.literal_eval(url_object)
        url_object['clicks'] = url_object['clicks'] + 1
        print url_object['clicks']
        store_object.create(code, url_object)
        return HttpResponseRedirect(url_object['url'])

def create(request):
    url = request.GET.get('url')
    short_code = hashlib.sha1(url).hexdigest()[0:6]
    store_object = Urls()
    url = store_object.fetch(short_code)

    if url is None:
        url = { 'url': url, 'created_at': int(time.time()),
                'clicks': 0, 'short_url': SHORT_URL_HOST %short_code }
        store_object.create(short_code, url)
    else:
        print 'Object already exists'

    return HttpResponse(short_code)