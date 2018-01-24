#! python3
class Dog():
    """ a test for simulate a dog"""

    def __init__(self, name, age):
        """ initiate name and age """
        self.name = name
        self.age = age

    def sit(self):
        """ simulate sit under order"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ simulate roll_over under order"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('Qiuqiu', 2)
print("My dog's name is %s." % my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
#print(my_dog)
print("\n")
your_dog = Dog('lucy', 2)
print("your dog's name is %s." % your_dog.name.title())
print("your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()