# coding=utf-8


import unittest
from city_functions import city_in_country


class CityTestCase(unittest.TestCase):
    """ 测试city_functions.py"""
    def test_city_country(self):
        """ 能够正确输出"""
        city_country = city_in_country('beijing', 'china')
        self.assertEqual(city_country, 'Beijing, China')


unittest.main()
'''
city_country = city_in_country('beijing', 'china')
print(city_country)
'''