file_path = '/Users/dell/mystuff/new_file.txt'
with open(file_path) as file_object:
	contents = file_object.read()
print(contents.rstrip())