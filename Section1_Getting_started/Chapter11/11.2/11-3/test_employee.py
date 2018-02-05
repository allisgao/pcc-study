# coding=utf-8

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """test employee"""

    def test_give_default_raise(self):
        """test default rise"""
        employee = Employee('Jackson', 'Michal', 5000000)
        salaries = employee.give_rise()
        self.assertEqual(5005000, salaries)

    def test_give_custom_raise(self):
        """test custome rise"""
        employee = Employee('WashingTon', 'Jorge', 10000000)
        salaries = employee.give_rise(100000)
        self.assertEqual(10100000, salaries)

unittest.main()


