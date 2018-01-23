#! python3

def making_cars(vender, type, **info):
    my_car = {}
    my_car['vender'] = vender
    my_car['type'] = type
    for key, value in info.items():
        my_car[key] = value
    return my_car

mycar = making_cars('subaru', 'outback', color='blue', tow_package=True)
print(mycar)
