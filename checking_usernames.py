current_users = ['jacob', 'ilyssa', 'jaiden', 'james', 'adam']
new_users = ['james', 'bob', 'evan', 'susan', 'jacob']

current_users = [x.lower() for x in current_users]
new_users = [x.lower() for x in new_users]

for new_user in new_users:
	if new_user in current_users:
		print(f"The username, {new_user} is already used. Please enter a new username.")
	else:
		print(f"The username, {new_user} is available!")