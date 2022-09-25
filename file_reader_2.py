with open('pi_digits.txt') as file_object:
	# This file is able to be tampered with line by line.
	for line in file_object:
		print(line.rstrip())