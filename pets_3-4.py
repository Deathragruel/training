# Animal type is written after pet name because a non-default paremeter cannot
# follow a default paremeter
def describe_animal(pet_name, animal_type = 'dog'):
	"""Display information about a pet"""
	print(f"I have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.\n")

# A dog named Willie.
describe_animal('willie')
describe_animal(pet_name = 'willie')

# A hamster named Harry.
describe_animal('harry', 'hamster')
describe_animal(pet_name = 'harry', animal_type = 'hamster')
describe_animal(animal_type = 'hamster', pet_name = 'harry')