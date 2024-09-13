from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def About(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render())

def Contact(request):
    template = loader.get_template('Contact.html')
    return HttpResponse(template.render())
