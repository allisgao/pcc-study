#! python3
num = input("Please input a number: \n")

if int(num) % 10 == 0:
    print("%s is 10's integer multiples." % (num))
else:
    print("%s is not 10's integer multiples." % (num))