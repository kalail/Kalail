from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('kalail.main.views',
	url(r'^$', 'index'),
	url(r'^sign_out/$', 'sign_out'),
	)