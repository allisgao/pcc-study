#! python3
class Car():
    """a test for simulate a car"""
    def __init__(self, make, model, year):
        """initialize the attribute of a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """return description infomartion in tidy"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
