#! python3

from random import randint

class Die():

    def __init__(self, size=6):
        """initiaize"""
        self.size = size

    #def roll_die(self, size):
    def roll_die(self,):
        x = randint(1, self.size)
        print("This object have %s sizes, \nthe result is %s." % (self.size, x))


