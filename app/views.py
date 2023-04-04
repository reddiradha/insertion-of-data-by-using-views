from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    tn=input('enter topic ')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()

    return HttpResponse('topic inserted ')

def insert_webpage(request):
    tn=input('enter topic ')
    w1=input('enter name ')
    w2=input('enter url ')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wo=Webpage.objects.get_or_create(topic_name=To,name=w1,url=w2)[0]
    Wo.save()
    return HttpResponse('webpage inserted successfully')

def insert_accessrecord(request):
    tn=input('enter topic ')
    w1=input('enter name ')
    w2=input('enter url ')
    a1=input('enter author ')
    a2=input('enter date ')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    Wo=Webpage.objects.get_or_create(topic_name=To,name=w1,url=w2)[0]
    Wo.save()

    Ao=Accessrecord.objects.get_or_create(name=Wo,author=a1,date=a2)[0]
    Ao.save()

    return HttpResponse('aceess records inserted successfuly')
    
    