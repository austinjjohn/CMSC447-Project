from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import django.contrib.contenttypes
from .forms import RegisterationForm
from Haven.models import EvacLocation
from Haven.models import Login
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render({}, request))


def logout_user(request):
    logout(request)
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render({}, request))


def signup(response):
    if response.method == "POST":
        form = RegisterationForm(response.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(response, user)
            return redirect("homepage")  # UNCOMMENT WHEN WE HAVE A LISTINGS PAGE TO CONTINUE TO

    else:
        form = RegisterationForm()
    return render(response, "signup.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In.")
            return redirect('homepage')

        else:
            messages.error(request, "Incorrect Email or Password. Try Again.")
            return redirect('login')

    else:
        return render(request, 'login.html', {})


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

            # dog = request.POST['dog']
            # cat = request.POST['cat']
            # fish = request.POST['fish']
            # bird = request.POST['bird']
            # baby = request.POST['baby']
            # kid = request.POST['kid']
            if ("dog" in request.POST.keys()):
                dog = request.POST["dog"]
            else:
                dog = False
            if ("cat" in request.POST.keys()):
                cat = request.POST["cat"]
            else:
                cat = False
            if ("fish" in request.POST.keys()):
                fish = request.POST["fish"]
            else:
                fish = False
            if ("bird" in request.POST.keys()):
                bird = request.POST["bird"]
            else:
                bird = False
            if ("baby" in request.POST.keys()):
                baby = request.POST["baby"]
            else:
                baby = False
            if ("kid" in request.POST.keys()):
                kid = request.POST["kid"]
            else:
                kid = False

            # check if current listing data will be a duplicate
            isDuplicate = False
            for object in data:
                if object.get_address() == address:
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

def reserve(request, listing):
    chosenListing = listing
    data = EvacLocation.objects.all()
    reserving_username = request.POST.get('username')
    for location in data:
        if location.areEqual(chosenListing):
            if location.notDuplicateEvacuee(reserving_username):
                location.decrement_spaces(chosenListing.get_spaces())
                location.append_evac_reserved(reserving_username)
                location.save()

    return render(request, 'templates/listings.html', dict)

def volunteer(request):
    template = loader.get_template("volunteer_profile_page.html")
    return HttpResponse(template.render({}, request))


def map(request):
    template = loader.get_template("map.html")
    return HttpResponse(template.render({}, request))


def homepage(request):
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render({}, request))


def evacuee(request):
    template = loader.get_template("evac_profile_page.html")
    return HttpResponse(template.render({}, request))


def map(request):
    template = loader.get_template("map.html")
    return HttpResponse(template.render({}, request))

