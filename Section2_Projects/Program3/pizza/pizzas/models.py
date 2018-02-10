from django.db import models

# Create your models here.

class Pizza(models.Model):
    """ define a model named Pizza"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """ return name"""
        return self.name.title()

class Topping(models.Model):
    """
    pizza - foreignkey - Pizza
    name - put dosings
    """
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'topping'

    def __str__(self):
        return self.name


