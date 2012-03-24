from django.db import models
from time import gmtime, strftime
from events.utils import get_venue_info, get_fs_key

class Venue(models.Model):
    fs_id = models.CharField(max_length=100, blank=True)
    fs_name = models.CharField(max_length=200, blank=True)
    fs_verified = models.CharField(max_length=200, blank=True)
    fs_twitter = models.CharField(max_length=200, blank=True)
    fs_phone = models.CharField(max_length=200, blank=True)
    fs_address = models.CharField(max_length=200, blank=True)
    fs_cross_street = models.CharField(max_length=200, blank=True)
    fs_city = models.CharField(max_length=200, blank=True)
    fs_state = models.CharField(max_length=200, blank=True)
    fs_zip = models.CharField(max_length=200, blank=True)
    fs_country = models.CharField(max_length=200, blank=True)
    fs_geolat = models.DecimalField(null=True, blank=True,
                                    max_digits=10, decimal_places=7)
    fs_geolong = models.DecimalField(null=True, blank=True,
                                     max_digits=10, decimal_places=7)
    fs_distance = models.CharField(max_length=200, blank=True,)

    def __unicode__(self):
        return self.fs_name

    def save(self):
        venue = get_venue_info(self.fs_id)
        for field in self._meta.fields:
            if field.name != 'id' and field.name != 'fs_id':
                fs_keys = get_fs_key(field.name).split('.')
                val = venue
                for key in fs_keys:
                    if key in val:
                        val = val[key]
                    else:
                        val = ''
                setattr(self, field.name, val)
        super(Venue, self).save()


class Organization(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    
    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    all_day = models.BooleanField()
    url = models.URLField(max_length=200)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        #return self.start_date.strftime("The date is %A (%a) %d/%m/%Y")
        return self.name
