prompt = "\nEnter quit if you want to leave the program."
prompt += "\nTell me something and i will repeat it back to you: "
active = True

while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)