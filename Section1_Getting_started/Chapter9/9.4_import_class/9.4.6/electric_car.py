#! python3


from car import Car


""" a class to express EC"""

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

