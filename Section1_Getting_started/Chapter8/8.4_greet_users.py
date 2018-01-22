#! python3

def greet_usesrs(names):
    '''say greet to all in list'''
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_usesrs(usernames)









