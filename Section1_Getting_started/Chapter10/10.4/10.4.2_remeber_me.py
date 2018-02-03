#! python3

import json

username = input("What's your name?\n")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remeber you if you come back, %s." % username)


