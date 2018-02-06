from django.contrib import admin

# Register your models here.

# import models
from pizzas.models import Pizza, Topping

# register models
admin.site.register(Pizza)
admin.site.register(Topping)








