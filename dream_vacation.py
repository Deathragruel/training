dream_vacation = {}

while True:
	name = input("What is your name? ")
	prompt = "If you have a chance to visit any place in the world once,"
	prompt += " where would you go? "
	response = input(prompt)
	dream_vacation[name] = response
	repeat = input("Would you like to have another person take this poll?(yes/no) ")
	if repeat == 'no':
		break
print("\n--- Poll results ---")
for name, response in dream_vacation.items():
	print(f"{name} would like to go to {response}.")