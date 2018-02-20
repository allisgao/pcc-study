from django.urls import path
from . import views

# namespace
app_name = 'pizzas'
urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza')
]