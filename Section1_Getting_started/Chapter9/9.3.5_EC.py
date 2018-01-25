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

class Battery():
    """ try to simulate a EC-battery"""
    def __init__(self, battery_size=70):
        """initialize the EC-battery's attribute"""
        self.battery_size = battery_size

    def describe_battery(self):
        """ print a message describing the capacity of the EC-batery"""
        print("This car has a %s-kWh battery." % str(self.battery_size))

    def get_range(self):
        """ print a message to show the battery's continution of journey"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
         initialize the par-class's attribute
         initialize the attribute which EC specially have
         """
        super().__init__(make, model, year)
        self.battery = Battery()



'''
    def describe_battery(self):
        """ print a message describing the battery"""
        print("This car has a %s-kWh battery." % str(self.battary_size))

    def fill_gas_tank(self):
        """ EC have non tank"""
        print("This car doesn't need a gas tank.")
'''
''''''

my_tesla = ElectricCar('telsa', 'model s', 2016)
print(my_tesla.get_descriptive_name())
'''
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
'''
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()











"""
my_used_car = Car('audi', 'a4', 2016)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
"""
