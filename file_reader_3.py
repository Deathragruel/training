with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()
# This file can be tampered with, as it is, now, in the form of a list(lines).
for line in lines:
	print(line.rstrip())