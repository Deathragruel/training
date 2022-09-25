def make_pizza(size, *toppings):
	""" Print the list of toppings that have been requested. """
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(" -" + topping.title())
# This is a module used by the programs:- making_pizzas.py
#                                       - making_pizzas-2.py
#                                       - making_pizzas-3.py
#                                       - making_pizzas-4.py
#                                       - making_pizzas-5.py