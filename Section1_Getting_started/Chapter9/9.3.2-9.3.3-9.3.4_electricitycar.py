#! python3
class Car():
    """a test for simulate a car"""
    def __init__(self, make, model, year):
        """initialize the attribute of a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return description infomartion in tidy"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """print a message contains the miles infomartion"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """set the value"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """set the value to a certain value"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """ EC have non tank"""
        print("This car have a gas tank.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
         initialize the par-class's attribute
         initialize the attribute which EC specially have
         """
        super().__init__(make, model, year)
        self.battary_size = 70

    def describe_battery(self):
        """ print a message describing the battery"""
        print("This car has a %s-kWh battery." % str(self.battary_size))

    def fill_gas_tank(self):
        """ EC have non tank"""
        print("This car doesn't need a gas tank.")

''''''

my_tesla = ElectricCar('telsa', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()











"""
my_used_car = Car('audi', 'a4', 2016)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
"""
