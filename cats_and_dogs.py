def read_file(filename):
	""" A function to display certain files(assignment). """
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		pass
	else:
		print(contents)
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	read_file(filename)
	print("\n")