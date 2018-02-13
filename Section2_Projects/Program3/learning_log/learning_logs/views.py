from django.shortcuts import render
from .models import Topic

from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    """ learning_logs' index page"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """ show all topics """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """ show single topic and its items"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """ add new topic"""
    if request.method != 'POST':
        # didn't submit datas: creat a new form
        form = TopicForm()
    else:
        # POST submited data, solve the data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """ add new items/entry to special topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # didn't submit datas, create an empty form
        form = EntryForm()
    else:
        # POST submited data, deal with the date
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


