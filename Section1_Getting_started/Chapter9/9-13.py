#! python3

from collections import OrderedDict

my_dict = {'zoo': 'a place to see animals.',
           'lucky': 'have a good fortain.',
           'pc': 'personal computer',
           'human': 'humanbeings',
           'fish': 'tastes good'
           }
for key,value in my_dict.items():
    print(key + '  :  ' + value)