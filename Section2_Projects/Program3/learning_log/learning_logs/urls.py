""" define learning_logs' URL pattern"""
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # homepage
    # url(r'^$', views.index, name='index')
    path('', views.index, name='index'),
]
