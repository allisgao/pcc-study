#! python3

filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object.readlines():
        line = line.replace('Python', 'C')
        print(line.rstrip())