from random import choice

def lottery():
	lottery_values = [13, 89, 54, 29, 499, 344, 232, 1, 3233, 873, 'A', 'U', 'R',
	                  'O', 'E']
	print("Any ticket matching the following four numbers or"
	      " letters wins a prize!\n (They are randomized):")
	one = choice(lottery_values)
	two = choice(lottery_values)
	if two == one:
		two = choice(lottery_values)
	three = choice(lottery_values)
	if three == two or three == one:
		three = choice(lottery_values)
	four = choice(lottery_values)
	if four == three or four == two or four == one:
		four = choice(lottery_values)

	print(one)
	print(two)
	print(three)
	print(four)

	my_ticket = [13, 89, 54, 29, 499, 344, 232, 1, 3233, 873, 'A', 'U', 'R',
	                  'O', 'E']
	print("\nMy ticket:")
	for ticket in my_ticket:
		result = ticket
		if result == one or result == two or result == three or result == four:
			print(f"{result}\n You win!")
			print(my_ticket.index(result))
			break

lottery()