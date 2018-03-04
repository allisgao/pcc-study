from die import Die
import pygal

# create a D6
die_1 = Die()
die_2 = Die()
die_3 = Die()
# roll die some times, and store the result in a list
results = []
for roll_number in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# analize the resultes
frequencies = []
max_result = die_1.number_sides + die_2.number_sides + die_3.number_sides
# 一个骰子最小数是1，最大数是骰子的面数，即掷骰子的范围在这个范围内；
# 以此类推，n个骰子最小数是n，最大数是骰子面数之和，即掷骰子和数在这个范围内。
for value in range(3, max_result + 1):
    frequencey = results.count(value)
    frequencies.append(frequencey)


# visualize the result
hist = pygal.Bar()

hist.title = "Results of rolling 3 D6 10000 times."
hist.x_labels = [i for i in range(3,19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
