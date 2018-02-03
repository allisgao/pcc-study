#! python3
import os

filenames = ['cats.txt', 'dogs.txt']
filepath = "E:\\MyCodes\\python\\pcc\\Section1_Getting_started\\Chapter10\\10.3\\10-8"

for filename in filenames:
    file = os.path.join(filepath, filename)
    try:
        with open(file) as f_obj:
            print(f_obj.read())
    except FileNotFoundError:
        print("File %s not found." % filename)