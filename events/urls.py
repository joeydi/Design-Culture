from django.conf.urls.defaults import *

urlpatterns = patterns('events.views',
	(r'^$', 'index'),
	(r'^(?P<event_id>\d+)/$', 'detail'),
)