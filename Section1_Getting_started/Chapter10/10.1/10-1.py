#! python3

filename = 'learning_python.txt'

with open(filename) as file_object:
    print(file_object.read())

print("\n")

with open(file_object) as file_object:
    for line in file_object.readlines():
        print(line)