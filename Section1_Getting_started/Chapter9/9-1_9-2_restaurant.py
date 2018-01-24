#! python3

class Restaurant():
    def __init__(self, r_name, r_cuisine_type):
        self.name = r_name.title()
        self.ctype = r_cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is %s" % self.name.title())
        print("The cuisine type of this restaurant is %s." % self.ctype)

    def open_restaurant(self):
        print("%s is in bussiness." % self.name.title())

restaurant = Restaurant('quanjude', 'rostduck')
print(restaurant.name)
print(restaurant.ctype)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n9-2:\n")
m_rstant = Restaurant('donglaishun', 'vegetable')
m_rstant.describe_restaurant()
print("\n")
m_rstant2 = Restaurant('daoxiangcun', 'cake')
m_rstant2.describe_restaurant()
print("\n")
m_rstant3 = Restaurant('shifenzhong', 'kuaican')
m_rstant3.describe_restaurant()
