def get_formatted_name(first_name, last_name):
	""" Return a full name, neatly formatted. """
	full_name = f"{first_name} {last_name}"
	return full_name.title()
	# This is an infinite loop!
while True:
	print("\nEnter q at an any time to quit the loop.")
	print("Please tell me your name: ")
	first = input("First name: ")
	if first == 'q':
		break
	last = input("Last name: ")
	if last == 'q':
		break
	name = get_formatted_name(first, last)
	print(f"\nHello, {name}!")