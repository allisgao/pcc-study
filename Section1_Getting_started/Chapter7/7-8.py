# coding=utf-8
sandwich_orders = ['san1', 'san2', 'san3', 'san4']
finished_sandwichs = []

while sandwich_orders:
    f_swch = sandwich_orders.pop()
    finished_sandwichs.append(f_swch)
    print("I made your %s sandwich." % (f_swch.title()))

print("\nFinished.")
for f_swch in finished_sandwichs:
    print("%s sandwich is made." % (f_swch.title()))
