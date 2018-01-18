#! python3

# ask how many peoples
num = input("Please input how many peoples:\n")
# if number > 8, no free tables.
"""
num = int(num)
if num > 8:
"""
if int(num) > 8:
    print("Sorry, We donnot have a free table for %s peoples." % (str(num)))
else:
    print("Yes, please.")


