#! python3
## need some adjusting.
class User():
    def __init__(self, firstname, lastname, **info):
        self.fname = firstname
        self.lname = lastname
        self.login_attempts = 0
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

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("attempts: %s" % str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("attempts: %s" % str(self.login_attempts))

class Admin(User):
    """ a administrator"""
    def __init__(self, firstname, lastname, **info):
        super().__init__(firstname, lastname, **info)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The administrator's privileges are: ")
        for i in self.privileges:
            print(" - " + i)


user1 = User('albert', 'einstain', field='physicial')
user1.describe_user()
user1.greet_user()
print("")

admin1 = Admin('gao', 'jing', location='china')
#admin1.show_privileges()
print(admin1.show_privileges())

