preferable_dinner_invitees = ['Sulaiman (A.S)', 'Tayyip Erdogan', 'Random Cavemen from when humans first lived on Earth']
print(f"I want to know the average personality of parrots. Please come and eat dinner with me, {preferable_dinner_invitees[0]}.")
print(f"I want to know how to annihilate corruption. Please come and eat dinner with me, {preferable_dinner_invitees[1]}.")
print(f"Do you want to see a device that can allow you to communicate with anyone you know on Earth,\n even if they are on the other side of the planet and which can access almost all information on Earth?\n Then you, {preferable_dinner_invitees[2]}, can come and eat dinner with me.")
print(f"{len(preferable_dinner_invitees)} guests? ok.")

print(f"Really? Ah, i see. Okay then, next time. Ugh. It seems that {preferable_dinner_invitees[1]} cannot make it.\n I have to think of a different person to invite.")
preferable_dinner_invitees[1] = 'Elon Musk'
print(preferable_dinner_invitees)
print(f"Although a little late, we are inviting you, {preferable_dinner_invitees[1]}, to our dinner as\n we would like to know how you made so much money in such a small amount of time and what skills were required.")
print(f"{len(preferable_dinner_invitees)} guests? ok.")

print("A new and bigger dinner table, really? Okay then. I'll invite a few more guests as well then.")
preferable_dinner_invitees.insert(1, 'Alien')
preferable_dinner_invitees.insert(3, 'Keiichi Maebara')
preferable_dinner_invitees.append('Albert Einstein')
print(preferable_dinner_invitees)
print(f"This is an invitation for you, Mr.{preferable_dinner_invitees[1]} to dinner, so we can discuss interspecies relations.")
print(f"We expect your arrival to this dinner, {preferable_dinner_invitees[3]} to discuss what happened after June 1983 in Hinamizawa.")
print(f"{preferable_dinner_invitees[-1]}, your arrival is of utmost importance as we\n want to warn you of the possible dangers of the research you are conducting.")
print(f"{len(preferable_dinner_invitees)} guests? ok.")

print("No way!. Only two guests? Fine. I'll sent the messages of apologies.")
remove_guest = preferable_dinner_invitees.pop()
print(f"I am very sorry, {remove_guest}, that our dinner table could not make it in so we do not have space for you anymore. My apologies\n but i hope you understand our situation. I am sorry.")
remove_guest_2 = preferable_dinner_invitees.pop()
print(f"I am very sorry, {remove_guest_2}, that our dinner table could not make it in so we do not have space for you anymore. My apologies\n but i hope you understand our situation. I am sorry.")
remove_guest_3 = preferable_dinner_invitees.pop()
print(f"I am very sorry, {remove_guest_3}, that our dinner table could not make it in so we do not have space for you anymore. My apologies\n but i hope you understand our situation. I am sorry.")
remove_guest_4 = preferable_dinner_invitees.pop()
print(f"I am very sorry, {remove_guest_4}, that our dinner table could not make it in so we do not have space for you anymore. My apologies\n but i hope you understand our situation. I am sorry.")
print(f"{len(preferable_dinner_invitees)} guests? ok.")

print(f"We are still expecting your visit, {preferable_dinner_invitees[0]}.")
print(f"We are still expecting your visit, {preferable_dinner_invitees[1]}.")
del preferable_dinner_invitees[0]
del preferable_dinner_invitees[0]
print(f"{len(preferable_dinner_invitees)} invitations? ok.")