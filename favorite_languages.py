favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

preferable_candidates_for_poll = ['sarah', 'bob', 'edward', 'jonathan', 'sam']

print("\nPoll candidates:")
for preferable_candidate_for_poll in preferable_candidates_for_poll:
	
	if preferable_candidate_for_poll in favorite_languages.keys():
		print(f"Thank you, {preferable_candidate_for_poll.title()}, for responding!")
	
	else:
		print(f"Please take our poll, {preferable_candidate_for_poll.title()}")