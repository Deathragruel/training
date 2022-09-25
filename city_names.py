def city_country(city, country):
	location = f"{city.title()}, {country.title()}"
	return location
area_1 = city_country('lahore', 'pakistan')
print(area_1)
area_2 = city_country('dhaka', 'bangladesh')
print(area_2)
area_3 = city_country('calcutta', 'india')
print(area_3)