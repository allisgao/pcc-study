# coding=utf-8

class Employee():
    """ a class test - employee"""

    def __init__(self, lastname, firstname, salary):
        """ initialize """
        self.lastname = lastname
        self.firstname = firstname
        self.salary = salary

    def give_rise(self, rise_salary=5000):
        """ rising salarys, default is 5000"""
        salarys = self.salary + rise_salary
        return salarys

