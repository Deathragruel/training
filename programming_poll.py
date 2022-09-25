while True:
	print("Enter q if you want to leave.")
	response = input("Why did you start programming?: ")
	if response == 'q':
		break
	else:
		with open('programming_poll.txt', 'w') as file_object:
			file_object.write(response + '\n')

print("Your reason(s) have been stored in file: programming_poll.txt")