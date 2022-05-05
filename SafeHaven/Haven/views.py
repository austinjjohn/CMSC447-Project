from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import RegisterationForm
from Haven.models import EvacLocation
from Haven.models import Signup
# Create your views here.


def index(request):
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render({}, request))
    # return HttpResponse("Hello, world. You're at the Haven index.")

def login(response):
    if response.method == "POST":
        form = RegisterationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/listings") #UNCOMMENT WHEN WE HAVE A LISTINGS PAGE TO CONTINUE TO
    else:
        form = RegisterationForm()
    return render(response, "login.html", {"form": form})


def signup(request):
    if request.method == "POST":
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('username') and request.POST.get('password') and request.POST.get('email'):
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            username = request.POST["username"]
            password = request.POST["password"]
            email = request.POST["email"]

            signup = Signup.create(firstname, lastname, username, email, password)
            signup.save()

    data = Signup.objects.all()
    info = {
        "list_data": data
    }
    return render(request, 'signup.html', info)

    # if response.method == "POST":
    #     form = RegisterationForm(response.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect("/listings") #UNCOMMENT WHEN WE HAVE A LISTINGS PAGE TO CONTINUE TO
    # else:
    #     form = RegisterationForm()
    # return render(response, "signup.html", {"form": form})


def listings(request):
    # data is all evacLocations
    data = EvacLocation.objects.all()
    # creates dict to pass all the evacLocation instances
    info = {
        "list_data": data
    }
    # if a new location is being made from volunteer index
    if request.method == 'POST':
        if request.POST.get('address') and request.POST.get('spaces') and request.POST.get('username'):
            # grab data from post request to populate evaclocation object
            address = request.POST["address"]
            pets = request.POST["pets"]
            spaces = request.POST["spaces"]
            username = request.POST["username"]
            dog = request.POST['dog']
            cat = request.POST['cat']
            fish = request.POST['fish']
            bird = request.POST['bird']
            baby = request.POST['baby']
            kid = request.POST['kid']

            # check if current listing data will be a duplicate
            isDuplicate = False
            for object in data:
                if object.__str__() == address:
                    isDuplicate = True

            # only create evac location object & save to database if curr listing DNE in database already
            if not isDuplicate:
                # convert checkbox values to booleans
                if dog == 'on':
                    dog = True
                else:
                    dog = False
                if cat == 'on':
                    cat = True
                else:
                    cat = False
                if fish == 'on':
                    fish = True
                else:
                    fish = False
                if bird == 'on':
                    bird = True
                else:
                    cbirdat = False
                if baby == 'on':
                    baby = True
                else:
                    baby = False
                if kid == 'on':
                    kid = True
                else:
                    kid = False

                # create the new location and save to database
                location = EvacLocation.create(address, pets, spaces, username, dog, cat, fish, bird, baby, kid)
                location.save()

    # render the listings page with the info dict passed in
    return render(request, 'listings.html', info)


def volunteer(request):
    template = loader.get_template("volunteer_profile_page.html")
    return HttpResponse(template.render({}, request))


def evacuee(request):
    template = loader.get_template("evac_profile_page.html")
    return HttpResponse(template.render({}, request))

def createListing(request):
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
    return render(request, 'templates/listings.html', dict)

def map(request):
    template = loader.get_template("map.html")
    return HttpResponse(template.render({}, request))

