from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth import authenticate, login

#from .models import Evacuee, Volunteer, EvacLocation

# Create your views here.


def index(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render({}, request))
    #return HttpResponse("Hello, world. You're at the Haven index.")


def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render({}, request))


def listings(request):
    template = loader.get_template("listings.html")
    return HttpResponse(template.render({}, request))
    # return HttpResponse("Hello, world. You're at the listings index.")
