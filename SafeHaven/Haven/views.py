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
            return redirect("home")  # UNCOMMENT WHEN WE HAVE A LISTINGS PAGE TO CONTINUE TO

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
            address = request.POST["address"]
            pets = request.POST["pets"]
            spaces = request.POST["spaces"]
            username = request.POST["username"]

            # create the new location
            location = EvacLocation.create(address, pets, spaces, username)
            location.save()

    # render the listings page with the info dict passed in
    return render(request, 'listings.html', info)


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
