# coding=utf-8

import json


def get_stored_username():
    """if stored, fetch it"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """ notice user to input username"""
    username = input("What's your name?\n")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """ greet user, and show username"""
    username = get_stored_username()
    if username:
        print("Welcome back, %s." % username)
    else:
        username = get_new_username()
        print("We'll remeber you when you come back, %s." % username)


greet_user()
