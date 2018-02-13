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
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # new_topics, add new topics
    path('new_topic/', views.new_topic, name='new_topic'),

    # add new items
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # edit entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
