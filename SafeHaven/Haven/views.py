from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import RegisterationForm

#from .models import Evacuee, Volunteer, EvacLocation

# Create your views here.


def index(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render({}, request))
    #return HttpResponse("Hello, world. You're at the Haven index.")

def login(response):
    if response.method == "POST":
        form = RegisterationForm(response.POST)
        if form.is_valid():
            form.save()
        # return redirect("/listings") #UNCOMMENT WHEN WE HAVE A LISTINGS PAGE TO CONTINUE TO
    else:
        form = RegisterationForm()
    return render(response, "login.html", {"form": form})

# {"form": form}
# def login(request):
#     template = loader.get_template("login.html")
#     return HttpResponse(template.render({}, request))

def index(request):
    mapbox_access_token = 'pk.eyJ1Ijoiam1pMSIsImEiOiJjbDJndjV0b2kwN245M2tteHN3NTcwaXNpIn0.pOCxELPUcT3JC9rXzhL07Q'
    return render(request, 'map.html', {'mapbox_access_token': mapbox_access_token})
