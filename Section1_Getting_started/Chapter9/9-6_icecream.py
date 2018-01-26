#! python3

class Restaurant():
    def __init__(self, r_name, r_cuisine_type):
        self.name = r_name.title()
        self.ctype = r_cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is %s" % self.name.title())
        print("The cuisine type of this restaurant is %s." % (self.ctype))

    def open_restaurant(self):
        print("%s is in bussiness." % self.name.title())

class IcecreamStan(Restaurant):
    """ icecream"""
    def __init__(self, r_name, r_cuisine_type):
        """ initialize class from f-class"""
        super().__init__(r_name, r_cuisine_type)
        self.favors = []

    def add_favors(self, favorite):
        self.favors.append(favorite)
    def show_favors(self):
        print("My favorite Ice-Creams are: ")
        #print(self.favors)
        for i in self.favors:
            print(i)


my_icecream = IcecreamStan('Frice', 'self-canteen')
print(my_icecream.describe_restaurant())
my_icecream.add_favors('strabary')
my_icecream.add_favors('milk')
my_icecream.show_favors()



"""
restaurant = Restaurant('quanjude', 'rostduck')
#print(restaurant.name)
#print(restaurant.ctype)
restaurant.describe_restaurant()
restaurant.open_restaurant()
"""

