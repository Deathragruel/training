prompt = "\nEnter quit if you want to exit the program."
prompt += "\nPlease enter a topping you would like to be added to your pizza: "
active = True

while active:
	topping = input(prompt)
	if topping == 'quit':
		active = False
	else:
		print(f"Adding {topping}.")