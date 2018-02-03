#! python

import json

# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name?\n")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remeber you when you come back, %s!" % username)
else:
    print("Welcome back, %s!" % username)




