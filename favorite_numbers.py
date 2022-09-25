favorite_numbers = {
	'dwuaz': [7, 3],
	'chrisel87': [14, 7],
	'turn down for page 394': [8, 7, 3],
	'captain puffs': [17, 7],
	'aurora storm 12': [4, 2, 7],
}
for name, numbers in favorite_numbers.items():
	print("\nName:")
	print(f"\t{name.title()}")
	print("Favorite numbers:")
	for number in numbers:
		print(f"\t{number}")