sandwich_orders = ['chicken', 'pastrami', 'peanut butter and jelly', 'pastrami',
 'cheese', 'pastrami', 'egg']
finished_sandwiches = []

print("We have run out of pastrami. Are you happy now, dear customers?"
	"\nAre you happy now?! 'Cause FOR SOME REASON, LITERALLY EVERY ONE OF YOU\n"
	"WANTS PASTRAMI!!! sorry, i need a timeout...\n")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"I made your {sandwich.title()} sandwich!")
	finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
	print(f"\t{finished_sandwich.title()}")