cities = {
	'karachi': {
	'country': 'pakistan',
	'population': '11 million',
	'fact': 'commercial center',
	},
	'london': {
	'country': 'united kingdom',
	'population': '9 million',
	'fact': 'over 300 languages are spoken in london',
	},
	'moscow': {
	'country': 'russia',
	'population': '12 million',
	'fact': 'has the largest number of billionaires in the world',
	},
}
for name, city_info in cities.items():
	print("City name:")
	print(f"\t{name.title()}")
	country = f"{city_info['country']}"
	population = f"{city_info['population']}"
	fact = f"{city_info['fact']}"
	print(f"\t Location (country): {country.title()}")
	print(f"\t Population: {population.title()}")
	print(f"\t One Fact: {fact.title()}\n")