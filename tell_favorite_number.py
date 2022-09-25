import json

filename = 'favorite_number.json'

try:
	with open(filename) as f:
		tell = json.load(f)
except FileNotFoundError:
	prompt = input("What is your favorite number? ")
	with open(filename, 'w') as f:
		json.dump(prompt, f)
		print("I will remember that!")
else:
	print(f"I know your favorite number! It is {tell}.")