#! python3

#def print_modules(unprinted_designs, completed_modules):
def print_modules(unprinted_designs, completed_modules):
    """
    simulate each design-printing, until there is no unprinted designs
    printed items are moved to complete_modules
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: %s." % current_design)
        completed_modules.append(current_design)

def show_complete_models(completed_modules):
    """show all printed items"""
    print("\nThe following models have been printed: ")
    for completed_module in completed_modules:
        print(completed_module)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_modules(unprinted_designs[:], completed_models)
show_complete_models(completed_models)
