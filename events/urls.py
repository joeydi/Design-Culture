from django.conf.urls.defaults import *

urlpatterns = patterns('events.views',
	(r'^$', 'index'),
	(r'^events/(?P<event_id>\d+)/$', 'detail'),
)