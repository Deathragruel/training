usernames = []

if usernames:
	for username in usernames:
		if username == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello {username.title()}. Thank you for logging in again.")
else:
	print("We need to search for more users!")