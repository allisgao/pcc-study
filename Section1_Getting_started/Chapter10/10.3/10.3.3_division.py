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
    answer = int(first_num) / int(second_num)
    print(answer)