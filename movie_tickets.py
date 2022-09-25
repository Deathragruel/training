prompt = "\nPlease enter your age so we can determine the price of your movie ticket: "

while True:
	age = int(input(prompt))
	if age < 3:
		print("It is free.")
	elif age < 12:
		print("It costs 10$")
	else:
		print("It costs 15$")