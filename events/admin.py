from events.models import Event, Venue, Organization
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
	list_display = ('name', 'venue', 'start_date')

class VenueAdmin(admin.ModelAdmin):
	list_display = ('fs_name', 'fs_address', 'fs_city', 'fs_state')

admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Organization)