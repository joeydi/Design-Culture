import foursquare
from settings import FS_CLIENT_ID, FS_CLIENT_SECRET

def get_venue_info(venue_id):
    fs = foursquare.Foursquare(client_id=FS_CLIENT_ID, client_secret=FS_CLIENT_SECRET)
    venue = fs.venues(venue_id)
    return venue['venue']


fs_field_mapper = {
    'fs_name': 'name',
    'fs_verified': '',
    'fs_twitter': '',
    'fs_phone': 'contact.phone',
    'fs_address': 'location.address',
    'fs_cross_street': '',
    'fs_city': 'location.city',
    'fs_state': 'location.state',
    'fs_zip': 'location.postalCode',
    'fs_country': 'location.country',
    'fs_geolat': 'location.lat',
    'fs_geolong': 'location.lng',
    'fs_distance': '',
}


def get_fs_key(field_name):
    if field_name in fs_field_mapper:
        return fs_field_mapper[field_name]
    else:
        return ''