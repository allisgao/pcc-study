#! python3

def describe_pet(pet_name, animal_type='dog'):
    """"show pets information"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet('dog', 'Huohu')
#describe_pet('hamster', 'harry')

describe_pet('huzi')

describe_pet(pet_name='willile')

describe_pet(pet_name='harry', animal_type='hamster')