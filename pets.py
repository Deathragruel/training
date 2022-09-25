pet_0 = {'animal': 'dog', 'species': 'husky', 'owners_name': 'aron'}
pet_1 = {'animal': 'cat', 'species': 'american curl', 'owners_name': 'sarah'}
pet_2 = {'animal': 'parrot', 'species': 'indian ringneck',
'owners_name': 'aimen'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	print(f"Animal: {pet['animal'].title()}")
	print(f"\tSpecies: {pet['species'].title()}")
	print(f"\tOwner's name: {pet['owners_name'].title()}\n")