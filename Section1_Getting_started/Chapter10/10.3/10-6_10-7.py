#! python3

""" plus test"""

try:
    first_figure = int(input("Please input the first figure:\n"))
    second_figure = int(input("Please input the second figure:\n"))
    sum = first_figure + second_figure
    print("The sum is %s" % str(sum))
except ValueError:
    print("Please input an integer number.\nThe progress exited.")
