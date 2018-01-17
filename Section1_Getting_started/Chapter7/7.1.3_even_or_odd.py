#! python3
number = input("Enter a number, and I'll tell you if it's even or odd: \n")
#number = int(number)

if int(number) % 2 == 0:
    print("\nThe number %s is even" % (number))
else:
    print("\nThe number %s is odd." % number)