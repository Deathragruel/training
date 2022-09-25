major_rivers = {
	'nile': 'egypt',
	'euphrates': 'turkey',
	'indus': 'pakistan',
}
for rivers, countries in major_rivers.items():
	print(f"The river, {rivers.title()}, runs through {countries.title()}.")

print("\nThe following rivers are mentioned:")
for rivers in major_rivers.keys():
	print(f"{rivers.title()}")

print("\nThe following countries are mentioned:")
for countries in major_rivers.values():
	print(f"{countries.title()}")