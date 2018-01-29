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


class Battery():
    """ simulate EC's battery"""

    def __init__(self, batterysize=70):
        """ initialize the battery's attribute"""
        self.batterysize = batterysize

    def describe_battery(self):
        """ print a message to describe the volume of battery"""
        print("This car has a %s-kWh battery." % str(self.batterysize))

    def get_range(self):
        """ print a message to describe the continuation of the journey"""
        if self.batterysize == 70:
            range = 240
        elif self.batterysize == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """simulate the specialize of EC"""
    def __init__(self, make, model, year):
        """
        initialize the father-class's attribute, then initialize the special attribute of ECs
        """
        super().__init__(make, model, year)
        self.battery = Battery()