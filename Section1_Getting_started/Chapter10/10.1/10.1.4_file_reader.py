filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

#print(type(lines))
#print(lines)

for line in lines:
    print(line.rstrip())

