def describe_animal(animal_type, pet_name):
	"""Display information about a pet"""
	print(f"I have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.\n")

describe_animal(animal_type = 'hamster', pet_name = 'harry')
describe_animal(animal_type = 'dog', pet_name = 'willie')