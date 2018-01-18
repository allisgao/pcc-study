#! python3

""""""
while True:
    age = input("Please input your age:\n")
    if int(age) < 3:
        price = 'free'
        break
    elif 3 <= int(age) <12:
        price = '10'
        break
    else:
        price = '15'
        break
print("Yoru age is %s, and your ticket's price is %s" % (age,price))

"""
while True:
    age = input("Please input your age:\n")
    if int(age) < 3:
        price = 'free'
        print("Yoru age is %s, and your ticket's price is %s" % (age, price))
        continue
    elif 3 <= int(age) <12:
        price = '10'
        print("Yoru age is %s, and your ticket's price is %s" % (age, price))
        continue
    else:
        price = '15'
        print("Yoru age is %s, and your ticket's price is %s" % (age, price))
        continue
"""

#print("Yoru age is %s, and your ticket's price is %s" % (age,price))

