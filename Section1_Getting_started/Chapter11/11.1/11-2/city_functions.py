#! python3


def city_in_country(city, country, population=''):
    if population:
        city_country = city + ', ' + country + ' - population ' + str(population)
    else:
        city_country = city + ', ' + country
    return city_country.title()


'''
city_country = city_in_country('beijing', 'china', 5000000)
print(city_country)
'''