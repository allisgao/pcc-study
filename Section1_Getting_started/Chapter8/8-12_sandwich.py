#! python3

def make_sandwich(*toppings):
    print("\nMaking a sandwich need such toppings:")
    for topping in toppings:
        print(" -  %s" % topping)

make_sandwich('eggs')
make_sandwich('apple', 'orange', 'peal')
make_sandwich('chicken', 'milk', 'cheese', 'beckon')