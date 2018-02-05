# coding=utf-8

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """ test employee"""

    def setUp(self):
        """
        create an object for test
        """
        self.employee = Employee('Soray', 'Tom', 150000)
        self.raises = [5000, 10000]

    def test_give_default_rise(self):
        """ test default rise"""
        salaries = self.employee.give_rise()
        self.assertEqual(self.employee.salary + self.raises[0], salaries)

    def test_give_custom_rise(self):
        """ test custom rise"""
        salaries = self.employee.give_rise(self.raises[1])
        self.assertEqual(self.employee.salary + int(self.raises[1]), salaries)


unittest.main()