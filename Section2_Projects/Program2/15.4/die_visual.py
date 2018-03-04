from die import Die


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

print(frequencies)