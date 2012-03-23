import foursquare

def get_venue_info(venue_id):
	fs = foursquare.Foursquare()
	venue = fs.venue(venue_id)
	return venue['venue']