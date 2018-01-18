#! python3
age = input("Please input your age:\n")
while True:
    if int(age) < 3:
        price = 'free'
    elif 3 <= int(age) <12:
        price = '10'
    else:
        price = '15'
print("Yoru age is %s, and your ticket's price is %s" % (age,price))

