""" define learning_logs' URL pattern"""
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # homepage
    # url(r'^$', views.index, name='index')
    path('', views.index, name='index'),

    # show all topics
    path('topics/', views.topics, name='topics'),

    # details of special topics
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
