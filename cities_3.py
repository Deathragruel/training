def describe_city(name, country = 'pakistan'):
	print(f"{name.title()} is in {country.title()}.\n")

describe_city('lahore')
describe_city('dhaka', 'bangladesh')
describe_city(country = 'india', name = 'calcutta')