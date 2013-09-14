from django.conf.urls import patterns, url

urlpatterns = patterns('urlshortener.views',
		url(r'^shorten/', 'create'),
        url(r'^(?P<code>\w{1,50})', 'home'),
)
