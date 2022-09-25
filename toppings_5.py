available_toppings = ['mushrooms', 'olives', 'green peppers', 'pinapple',
'extra-cheese','pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra-cheese']

for requested_topping in requested_toppings:
	
	if requested_topping in available_toppings:

		print(f"Adding {requested_topping}.")

	else:

		print("Sorry. That topping is unavailable right now.")
print("We have finished making your pizza. Enjoy!")