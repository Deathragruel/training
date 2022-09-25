users = {
	'aenstein': {
	'first_name': 'albert',
	'last_name': 'einstein',
	'location': 'princeton',
	},
	'mcurie': {
	'first_name': 'marie',
	'last_name': 'curie',
	'location': 'paris',
	},
}
for username, user_info in users.items():
	print(f"Username: {username}")
	full_name = f"{user_info['first_name']} {user_info['last_name']}"
	location = f"{user_info['location']}"
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}\n")