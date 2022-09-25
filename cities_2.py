prompt = "\nEnter 'quit' when you want to leave the program."
prompt += "\nPlease enter the name of a city you have visited: "

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")