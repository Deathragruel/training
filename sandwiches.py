def make_sandwich(*items):
	print("The following is a summary of items wanted on a sandwich:")
	for item in items:
		print('- ' + item.title())

make_sandwich('mayonnaise', 'kebab', 'white sauce', 'onions')
make_sandwich('sauce', 'kebab')
make_sandwich('eggs', 'sauce', 'cucumber pieces')