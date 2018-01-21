#! python3

def describe_pet(animal_type, pet_name):
    """"show pets information"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet('dog', 'Huohu')
#describe_pet('hamster', 'harry')
describe_pet(animal_type="cat", pet_name="Zoophia")
describe_pet(pet_name="White_abi", animal_type="rabbit")