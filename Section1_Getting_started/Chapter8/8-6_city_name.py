#! python3

def city_country(city, country):
    my_str = city.title() + ', ' + country.title()
    return my_str

str1 = city_country('beijing', 'china')
print(str1)

