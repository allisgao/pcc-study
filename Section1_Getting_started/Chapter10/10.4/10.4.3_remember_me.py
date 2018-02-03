#! coding = utf-8

import json


def greet_user():
    """greet user, and point out user's name"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What's your name?\n")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We will remember you when you come back, %s!" % username)
    else:
        print("Welcome back, %s!" % username)


greet_user()