#! python3

filename = 'guest.txt'

with open(filename, 'a') as file_object:
    visitor_name = input("Please enter your name: \n")
    file_object.write(visitor_name.title() + '\n')


"""
    while True:
        visitor_name = input("Please Enter your name:\nPress Enter to exit.\n")
        if visitor_name != '':
            file_object.write(visitor_name.title() + '\n')
            #continue
 """


