#! python3

msg = "Please input sdgaesddes.\nEnter 'quit' to quit.\n"

a = ''

while a != 'quit':
    a = input(msg)
    if a != 'quit':
        print("We'll add %s to your pizza." % (a))
        continue