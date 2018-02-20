# coding=utf-8

""" define URL pattern for application named users """

from django.urls import path
from django.contrib.auth.views import login

from . import views
app_name = 'users'

urlpatterns = [
    # login page
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),

    # logout
    path('logout/', views.logout_view, name='logout'),

    # register
    path('register/', views.register, name='register'),

]



