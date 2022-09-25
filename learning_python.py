with open('learning_python.txt') as file_object:
	contents = file_object.read()
print(contents.rstrip())
print("\n")

with open('learning_python.txt') as file_object:
	lines = file_object
	for line in lines:
		print(line.rstrip())
print("\n")

with open('learning_python.txt') as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())