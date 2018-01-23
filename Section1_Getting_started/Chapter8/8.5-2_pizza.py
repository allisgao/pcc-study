#! python3
def make_pizza(*toppings):
    """describle pizza making in summary"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- %s" % topping)
make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')