# coding = utf-8

import json

'''
# storage
def get_stored_num():
    """ if number is stored, fetch it"""
    filename = 'f_num.json'
    try:
        with open(filename) as f_obj:
            f_num = json.load(f_obj)
    except FileNotFoundError:
        return  None
    else:
        return f_num
    
# fetch
def show_num():
    """show this number"""
    f_num = get_stored_num()
    if f_num:
        print("I know your favorite number! It's %s!" % str(f_num))
    else:
        f_num = input("")
'''

# notice user to input favorite number and storeit
filename = 'f_num.json'
f_num = input("Please enter your favorite number:\n")

with open(filename, 'w') as f_obj:
    json.dump(f_num, f_obj)
    #print("I have known your favorite number! \nIt's %s!" % str(f_num))

#TODO: show this number

with open(filename) as f_obj:
    f_num = json.load(f_obj)
    print("I know your favorite number! It's %s!" % str(f_num))










