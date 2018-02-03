# coding=utf-8
import json

""" get and store the number"""
def get_and_store_num():
    filename = 'f_num.json'
    try:
        with open(filename) as f_obj:
            f_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return f_num


""" fetche the number"""


def fetch_num():
    f_num = get_and_store_num()
    if f_num:
        print("I know your favorite number! It's %s." % str(f_num))
    else:
        f_num = input("Please enter your favorite number:\n")
        filename = 'f_num.json'
        with open(filename, 'w') as f_obj:
            json.dump(f_num, f_obj)
            print("Got it!")


fetch_num()

