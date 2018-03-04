# coding=utf-8

from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

# roll it many times, and storage the results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyse the results
frequencies = []
max_result = die_1.number_sides + die_2.number_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the result
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_d6-d10_visual.svg')
