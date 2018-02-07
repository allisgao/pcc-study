""" define pizzas' URL pattern"""

from django.shortcuts import render

# Create your views here.
def index(request):
    """ pizzas' index page"""
    return render(request, 'pizzas/index.html')


