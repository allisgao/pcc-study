#! python3


class Restaurant():
    """ some comments """
    def __init__(self, name, style):
        """ initialize"""
        self.name = name
        self.style = style

    def describe_restaurant(self):
        """ describe the restaurant """
        print("The restaurant name is %s, and it's style is %s." %( self.name.title(), self.style.title()))



