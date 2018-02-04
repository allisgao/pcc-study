# coding=utf-8


from name_function import get_formatted_name

print("Enter q at any time to quit.")
while True:
    first = input("\nPlease give me the first name:\n")
    if first == 'q':
        break
    last = input("\nPlease give me the last name:\n")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\n\tNeatly formatted name: %s." % formatted_name)