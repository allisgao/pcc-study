def make_pizza(size, *toppings):
    print("\nMaking a %s-inch pizza with the following toppings:" % str(size))
    for topping in toppings:
        print("- %s" % topping)

def greet(name):
    print("\nHello, %s!" % name)