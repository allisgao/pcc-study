#! python3
# some different
class Restaurant():
    def __init__(self, r_name, r_cuisine_type):
        self.name = r_name.title()
        self.ctype = r_cuisine_type
        self.snum = 0

    def describe_restaurant(self):
        print("The restaurant's name is %s" % self.name.title())
        print("The cuisine type of this restaurant is %s." % self.ctype)

    def open_restaurant(self):
        print("%s is in bussiness." % self.name.title())

    def number_served(self, snum):
        self.snum = snum

    def set_number_served(self, snum):
        self.snum += snum

    def read_num(self):
        print("We have served "  + str(self.snum) + " peoples." )



restaurant = Restaurant('quanjude', 'rostduck')
print(restaurant.name)
print(restaurant.ctype)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served(5654)
restaurant.set_number_served(26)
restaurant.read_num()
