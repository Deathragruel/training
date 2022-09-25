glossary = {
	'print': 'show',
	'del': 'delete',
	'list': 'a group of elements',
	'tuple': 'an immutable list',
	'sort': 'alphabetically organise (specifically, for lists(i think))',
	'get': 'show, but just in case it does not exist, show a replacement message to deal with errors',
	'sorted': 'alphabetically organise but temporarily (only for the command it is used in)',
	'reversed': 'reverse the order',
	'string': 'anything in between quotation marks or apostrophies',
	'variables': 'anything that is not a string and are used to represent values',
}
for terms, meanings in glossary.items():
	print(f"{terms}: {meanings}")