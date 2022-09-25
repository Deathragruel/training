# This is a module for printing models.py

def print_models(unprinted_designs, completed_models):

	# Stimulate printing each design until none are left.
	# Move each design to completed_models after printing.
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)


def display_completed_models(completed_models):
	# Display all completed designs
	print("\nThe following designs have been printed:")
	for completed_model in completed_models:
		print(completed_model)