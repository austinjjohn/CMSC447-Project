import datetime

from django.db import models
from django.utils import timezone
from django.contrib import auth
from django.forms.models import model_to_dict
from django import forms


# Create your models here.


class EvacLocation(models.Model):
    # Each evac location has these variables
    address = models.CharField(max_length=200)
    # pets = models.BooleanField(default=False)
    pets = models.CharField(max_length=50)  # converts to bool in views.py
    spaces = models.IntegerField(default=1)
    username = models.CharField(max_length=200)
    reservations = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.address

    def allows_pets(self):
        return self.pets

    def get_spaces(self):
        return self.spaces

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def is_full(self):
        return self.spaces <= self.reservations

    @classmethod
    def create(cls, address, pets, spaces, username):
        location = EvacLocation(address=address, pets=pets,
                                spaces=spaces, username=username, reservations=0,
                                pub_date=timezone.now())
        return location

    @classmethod
    def delete(cls):
        cls.delete()


class Signup(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    username = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def __str__(self):
        return self.firstname

    def __str__(self):
        return self.lastname

    def __str__(self):
        return self.username

    def __str__(self):
        return self.email

    def __str__(self):
        return self.password

    @classmethod
    def create(cls, firstname, lastname, username, email, password):
        signup = Signup(firstname=firstname, lastname=lastname, username=username, email=email, password=password)
        return signup

    @classmethod
    def delete(cls):
        cls.delete()


class Volunteer(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    def dict(self):
        return model_to_dict(self)


class Evacuee(models.Model):
    name = models.CharField(max_length=80)
    pets = models.IntegerField(default=0)
    spaces_needed = models.IntegerField(default=1)
    EvacLocation = models.ForeignKey(EvacLocation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def dict(self):
        return model_to_dict(self)
