#! python3

# create a list which contains num 1 to 1,000,000
my_list = [values for values in range(1,1000001)]

# use min() and max() to comfirm it began with 1 and end with 1,000,000
print("The min num is: " + str(min(my_list)))
print("The max num is: " + str(max(my_list)))

# use sum() to get the result
total = sum(my_list)
print("\nThe total is: " + str(total))
