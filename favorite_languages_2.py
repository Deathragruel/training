favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
print("Names:")
friends = ['phil', 'sarah']
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking our poll!")
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\tSo {name.title()} loves {language}!")
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(f"{language.title()}")

print("\nThese are the results:")
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

if 'erin' not in favorite_languages.keys():
	print("Erin! HOW DARE YOU FORGET TO TAKE OUR POLL! TAKE IT NOW!")