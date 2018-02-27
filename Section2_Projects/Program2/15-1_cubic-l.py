#! python3

import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, edgecolors='none', s=20)

# set char title and give names to x-axis and y-axis
plt.title("Cubic Nmubers", fontsize=20)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Cubic of Value", fontsize=10)

# set sizes of the scale
# plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([0, 5500, 0, 130000000000])

plt.show()




