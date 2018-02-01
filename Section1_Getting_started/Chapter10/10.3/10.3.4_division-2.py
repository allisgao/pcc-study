#! python3

# 待解决问题：如果除数不是整数，程序会提示，然后需要重新输first_num和second_num。

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
        try:
            answer = int(first_num) / int(second_num)
        except ZeroDivisionError:
            print("You can't divide by zero!")
        else:
            print(answer)
    except ValueError:
        print("Please enter an ingeger number to divide.")