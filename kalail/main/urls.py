from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('main.views',
	url(r'^$', 'index'),
	url(r'^sign_in_needed/$', 'sign_in_needed'),
	url(r'^sign_in/$', 'sign_in'),
	url(r'^about/$', 'about'),
	url(r'^contact/$', 'contact'),
	)