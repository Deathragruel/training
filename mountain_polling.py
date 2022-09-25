responses = {}
# Set the flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb some day? ")
	# Store the response in the dictionary.
	responses[name] = response
	# Find out if anyone else would like to take the poll.
	repeat = input("Would you like to let another person respond?(yes/no) ")
	if repeat == 'no':
		polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")