favorite_places = {
	'a lady never tells': ['chicago', 'coast(north carolina)'],
	'eb3031': ['berlin', 'paris'],
	'saubzilla': ['natural history museum(london)'],
}
for name, places in favorite_places.items():
	if name == 'eb3031':
		print("Name:")
		print(f"\t{name.upper()}")
		print("Favorite places:")
		for place in places:
			print(f"\t{place.title()}")
	
	elif name == 'saubzilla':
		print("Name:")
		print(f"\t{name.title()}")
		print("Favorite place:")
		for place in places:
			print(f"\t{place.title()}")
	else:
		print("Name:")
		print(f"\t{name.title()}")
		print("Favorite places:")
		for place in places:
			print(f"\t{place.title()}")