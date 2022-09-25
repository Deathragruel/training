pizzas = ['chicken tikka', 'fajita', 'cheese']
for pizza in pizzas:
	print(f"What kind of Pizza i like? Well, i love {pizza}. It's so delecious!")
print("Who wouldn't like pizza? An Alien? HA!")

friend_pizzas = pizzas[:]
pizzas.append('chili pepper')
friend_pizzas.append('hawaiian')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)