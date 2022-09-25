prompt = "\nEnter quit if you want to exit the program."
prompt += "\nPlease enter a topping you would like to be added to your pizza: "
topping = ""

while topping != 'quit':
	topping = input(prompt)
	if topping != 'quit':
		print(f"Adding {topping}.")