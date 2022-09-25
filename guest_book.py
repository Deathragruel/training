while True:
	print("Enter q if you want to leave.")
	name = input("Enter your name: ")
	if name == 'q':
		break
	else:
		print(f"Hello, {name}! Your visit has been recorded.")
		with open('guest.txt', 'a') as file_object:
			file_object.write(f"{name} visited.\n")