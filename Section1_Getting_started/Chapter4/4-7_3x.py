#! python3
# create the list

my_list = []
'''
# way1: division

for num in range(1,31):
    if num % 3 == 0:
        my_list.append(num)
'''
# way2: multiplication
for num in range(1,10):
    if num * 3 <= 30:
        my_list.append(num*3)


#print
for i in my_list:
    print(i)



