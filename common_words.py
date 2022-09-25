def find_common_word(filename):
	""" Finds the number of the common word demanded. """
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
		common = contents.lower().count('the ')
		print(common)

filenames = ['the_adventures_of_sherlock_holmes.txt', 'pride_and_prejudice.txt',
             'frankenstein.txt']
for filename in filenames:
	find_common_word(filename)