#! python3

sandwich_orders = ['san1', 'pastrami', 'san3', 'san4', 'pastrami', 'pastrami', 'pastrami']
print("The pastrami is sold out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("We only have such things:")
for i in sandwich_orders:
    print(i)



