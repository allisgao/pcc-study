#! python3

# create a list which contains cases to print
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
complated_modules = []

# simulate to print each design, until no unprinted
#  printed designs will be move to complate_modules[]
while unprinted_designs:
    current_dsgn = unprinted_designs.pop()

    # simulate the process
    print("Printing model: %s" % current_dsgn)
    complated_modules.append(current_dsgn)

# show printed design-modules
print("\nThe following models have been printed:")
for complated_module in complated_modules:
    print(complated_module.title())





