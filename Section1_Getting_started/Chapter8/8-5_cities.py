#! python3

def describe_city(city, country='china'):
    print("\n%s is in %s." %(city.title(), country.title()))

describe_city('beijing')
describe_city('tokyo')
describe_city('hancheng','korea')
