from die import Die


# create a D6
die = Die()

# roll die some times, and store the result in a list
results = []
for roll_number in range(100):
    result = die.roll()
    results.append(result)

print(results)