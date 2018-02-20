""" define pizzas' URL pattern"""

from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """ pizzas' index page"""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """ show all pizzas """
    pizzas = Pizza.objects.order_by('name')
    p_names = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', p_names)


def pizza(request, pizza_id):
    """ show single pizza and its details"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
