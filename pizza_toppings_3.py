prompt = "\nEnter quit if you want to exit the program."
prompt += "\nPlease enter a topping you would like to be added to your pizza: "

while True:
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print(f"Adding {topping}.")