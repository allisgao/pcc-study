# coding=utf-8

from random import randint

class Die():
    """ empress a die """

    def __init__(self, number_sides=6):
        """ die default have 6 sizes """
        self.number_sides = number_sides


    def roll(self):
        """ return a number between 1 and size's number"""
        return randint(1, self.number_sides)






