def make_shirt(size = 'large sized', message = 'I love Python!'):
	print(f"Your {size} shirt has been made with your requested message,"
		f" \n{message.title()}.\n")

make_shirt()
make_shirt('medium sized')
make_shirt(size = 'medium sized', message = "'fear is the mind killer'")