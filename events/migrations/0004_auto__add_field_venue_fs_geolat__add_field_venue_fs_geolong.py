# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Venue.fs_geolat'
        db.add_column('events_venue', 'fs_geolat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'Venue.fs_geolong'
        db.add_column('events_venue', 'fs_geolong', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Venue.fs_geolat'
        db.delete_column('events_venue', 'fs_geolat')

        # Deleting field 'Venue.fs_geolong'
        db.delete_column('events_venue', 'fs_geolong')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'all_day': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Organization']", 'null': 'True', 'blank': 'True'})
        },
        'events.organization': {
            'Meta': {'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'events.venue': {
            'Meta': {'object_name': 'Venue'},
            'fs_address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_cross_street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_distance': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_geolat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'fs_geolong': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'fs_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'fs_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_state': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_verified': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fs_zip': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['events']
