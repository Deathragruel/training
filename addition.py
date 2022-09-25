while True:
	print("Enter q if you want to quit.")
	print("Enter two numbers for addition.")
	try:
		number = input("Enter the first number for addition: ")
		if number == 'q':
			break
		number = int(number)
		number_2 = input("Enter the second number for addition: ")
		if number_2 == 'q':
			break
		number_2 = int(number_2)
	except ValueError:
		print("You cannot add words with numbers...")
	else:
		print(number + number_2)