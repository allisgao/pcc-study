#! python3

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quuit.")

while True:
    first_num = input("\nFirst number:\n")
    if first_num == 'q':
        break
    second_num = input("\nSecond number:\n")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
