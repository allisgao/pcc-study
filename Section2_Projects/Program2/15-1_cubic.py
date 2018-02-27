#! python3

import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=50)

# set char title and give names to x-axis and y-axis
plt.title("Cubic Nmubers", fontsize=20)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Cubic of Value", fontsize=10)

# set sizes of the scale
plt.tick_params(axis='both', which='major', labelsize=10)


plt.show()




