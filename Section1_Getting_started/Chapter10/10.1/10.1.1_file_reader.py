
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())
"""
# another expression method:
file_object = open('pi_digits.txt')
contents = file_object.read()
print(contents)
file_object.close()
"""