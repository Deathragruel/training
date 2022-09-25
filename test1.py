print("Hello there!. This is Robo Sam speaking. We shall begin the test you requested.")
print("Please choose what you prefer from the following options.")
print("Will you choose Apple, Bannana or Watermelon?")
fruit = input("Do answer word accurate ")
print("Ah", fruit)
print("Interesting choice. Let's continue")
human = input("Friend, Partner or Helper? ")
print("Really?", human)
print("Ok then")
weapon = input("Sword, Bat, or Gun")
print("The decision is clear then")
# Write code that will print the rest of the story commentary specifically if the reader had previously answered apple, helper and gun respectively
if fruit is Apple and human is Helper and weapon is Gun:
	print("You are the chosen one.")
	print("You can proceed into the back door. Remmember, do not hesitate.")
	print("So, he entered the room. He did not run away?. Oh well, Bygones be bygones.")
else:
	print("Pathetic. You failed. Leave and never return.")