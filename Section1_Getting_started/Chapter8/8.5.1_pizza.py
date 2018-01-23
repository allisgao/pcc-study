#! python3
def make_pizza(size, *toppings):
    print("\nMaking a %s-inch pizza with the following toppings:" % str(size))
    for topping in toppings:
        print("- %s" % topping)

make_pizza(6, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

