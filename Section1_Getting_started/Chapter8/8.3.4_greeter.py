#! python3

def get_formatted_name(fname, lname):
    full_name = fname + ' ' + lname
    return full_name.title()

while True:
    print('\nPlease tell me your name:')
    fname = input('First name:\n')
    if fname == 'q':
        break
    lname = input('Last name:\n')
    if lname == 'q':
        break
    formatted_name = get_formatted_name(fname,lname)
    print("\nHello, %s!" % formatted_name.title())




