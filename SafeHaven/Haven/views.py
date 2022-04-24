from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import RegisterationForm
from .models import EvacLocation

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

def listings(request):
    # template = loader.get_template("listings.html")
    # return HttpResponse(template.render({}, request))
    if request.method == 'POST':
        if request.POST.get('address') and request.POST.get('spaces'):
            address = request.POST["address"]
            pets = request.POST["pets"]
            spaces = request.POST["spaces"]
            dict = {
                'address': address,
                'pets': pets,
                'spaces': spaces
            }
            # location = EvacLocation.create(address, pets, spaces)
            # location.save()
            return render(request, 'listings.html', dict)

    else:
        return render(request, 'listings.html', dict)

def volunteer(request):
    template = loader.get_template("volunteer_profile_page.html")
    return HttpResponse(template.render({}, request))

def evacuee(request):
    template = loader.get_template("evac_profile_page.html")
    return HttpResponse(template.render({}, request))

# def createListing(request):
#     if request.method == 'POST':
#         if request.POST.get('address') and request.POST.get('spaces'):
#             address = request.POST["address"]
#             pets = request.POST["pets"]
#             spaces = request.POST["spaces"]
#             dict = {
#                 'address': address,
#                 'pets': pets,
#                 'spaces': spaces
#             }
#             return render(request, 'templates/listings.html', dict)
#
#     else:
#         return render(request, 'templates/listings.html', dict)
