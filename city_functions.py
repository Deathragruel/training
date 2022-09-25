def get_location(city, country, population = ''):
	""" Return a neatly formatted location named. """
	if population:
		location = f"{city}, {country}- population {population}"
	else:
		location = f"{city}, {country}"
	return location.title()