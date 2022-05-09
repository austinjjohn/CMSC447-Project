from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterationForm
from Haven.models import EvacLocation
from Haven.models import Login


# Create your views here.


def index(request):
    template = loader.get_template("homepage.html")
    return HttpResponse(template.render({}, request))
    # return HttpResponse("Hello, world. You're at the Haven index.")


def signup(response):
    if response.method == "POST":
        form = RegisterationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/listings")  # UNCOMMENT WHEN WE HAVE A LISTINGS PAGE TO CONTINUE TO
    else:
        form = RegisterationForm()
    return render(response, "signup.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('password'):
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage.html')
            else:
                messages.success(request, "Incorrect Email or Password. Try Again.")
                return redirect('login.html')

    #         logininfo = Login.create(firstname, lastname, username, email, password)
    #         logininfo.save()
    #
    # data = Login.objects.all()
    # info = {
    #     "list_data": data
    # }
    else:
        return render(request, 'login.html')

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
