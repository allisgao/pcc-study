# coding=utf-8


import json

filename = 'f_num.json'

try:
    with open(filename) as f_obj:
        f_num = json.load(f_obj)
except FileNotFoundError:
    f_num = input("Please input your favorte number:\n")
    with open(filename, 'w') as f_obj:
        json.dump(f_num, f_obj)
        print("Got it!\nIt's %s!" % f_num)
else:
    print("I know your favorite number!\nIt's %s!" % f_num)






