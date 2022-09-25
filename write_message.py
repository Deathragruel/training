with open('programming.txt', 'w') as file_object:
	file_object.write('I love programming.')
	file_object.write('\nI love creating new games.\n')
with open('programming.txt', 'a') as file_object:
	file_object.write("I also love finding meaning in large data sets.\n")
	file_object.write("I love creating apps that can run in a bowser.")