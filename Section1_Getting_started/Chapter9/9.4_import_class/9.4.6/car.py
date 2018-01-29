#! python3
""" a class to express cars"""


class Car():
    """ try to simulate cars"""
    def __init__(self, make, model, year):
        """ initialize the attribute describing cars"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ return tidy description"""
        long_name = str(self.year) + ' ' + self.make + ' '  + self.model
        return long_name.title()

    def read_odometer(self):
        """print a message to show the miles"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        set the mile to the pointed value
        refuse to re-config the miles.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ add the pointed value to miles"""
        self.odometer_reading += miles
