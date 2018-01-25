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


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(12)
my_new_car.read_odometer()