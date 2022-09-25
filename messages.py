def send_messages(messages, sent_messages):
	""" Removes each message from messages and transfers it to sent_messages
	    while printing each message to show that it is being sent """
	while messages:
		current_message = messages.pop()
		print(f"Sending:\t{current_message}")
		sent_messages.append(current_message)


def show_messages(sent_messages):
	""" Displays each message in sent_messages one by one"""
	for sent_message in sent_messages:
		print(f"{sent_message}")


messages = ['Hello everyone!', 'I am very cool.', 'Usama is stupid.']
sent_messages = []
send_messages(messages[:], sent_messages)
show_messages(sent_messages)

print(messages)
print(sent_messages)