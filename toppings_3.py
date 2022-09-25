requested_toppings = ['mushrooms', 'green peppers', 'extra-cheese']

for requested_topping in requested_toppings:

	if requested_topping == 'green peppers':
		print("Sorry. Green peppers are unavailable right now.")

	else:
		print(f"Adding {requested_topping}.")

print("We have finished making your pizza. Enjoy!")