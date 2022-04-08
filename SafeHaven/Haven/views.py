from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
    #return render(request, 'base.html')
    return HttpResponse("Hello, world. You're at the Haven index.")

def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render({}, request))
