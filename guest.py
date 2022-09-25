name = input("Enter your name: ")

with open('guest.txt', 'w') as file_object:
	file_object.write(name.title())