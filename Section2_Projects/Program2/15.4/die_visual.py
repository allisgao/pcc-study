from die import Die
import pygal

# create a D6
die = Die()

# roll die some times, and store the result in a list
results = []
for roll_number in range(1000):
    result = die.roll()
    results.append(result)

# analize the resultes
frequencies = []
for value in range(1, die.number_sides + 1):
    frequencey = results.count(value)
    frequencies.append(frequencey)


# visualize the result
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
