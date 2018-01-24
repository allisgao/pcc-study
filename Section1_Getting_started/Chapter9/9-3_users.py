#! python3

class User():
    def __init__(self, firstname, lastname, **info):
        self.fname = firstname
        self.lname = lastname
        for key, value in info.items():
            #infos = {}
            self.key = key
            self.value = value

    def describe_user(self):
        """print the user's information in subscribe"""
        print("The user's name is %s %s." % (self.fname.title(), self.lname.title()))
        print(self.fname.title() + ' ' + self.lname.title() + "'s %s is %s." % (self.key, self.value))

    def greet_user(self):
        print("Nice to meet you, %s" %(self.fname.title() + ' ' + self.lname.title()))

user1 = User('albert', 'einstain', field='physicial')
user1.describe_user()
user1.greet_user()
print("\n")
user2 = User('George', 'gao', location='China', favorite_fruit='orange', birthday='1991-12-13')
user2.describe_user()
user2.greet_user()


