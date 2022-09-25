# This code uses the module printing_functions.py
import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.display_completed_models(completed_models)