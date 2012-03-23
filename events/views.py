from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from events.models import Event
from datetime import datetime

def index(request):
	index_format = 'grid'
	upcoming_events_list = Event.objects.filter(start_date__gte=datetime.now()).order_by('start_date')
	return render_to_response('events/index.html', {'upcoming_events_list': upcoming_events_list, 'index_format': index_format})
	
def detail(request, event_id):
	e = get_object_or_404(Event, pk=event_id)
	return render_to_response('events/detail.html', {'event': e})