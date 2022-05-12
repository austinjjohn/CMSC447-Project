import datetime

from django.db import models
from django.utils import timezone
from django.contrib import auth
from django.forms.models import model_to_dict

from django import forms

# Create your models here.


class EvacLocation(models.Model):
    address = models.CharField(max_length=200)
    # pets = models.BooleanField(default=False)
    pets = models.CharField(max_length=50, default='NONE')  # converts to bool in views.py
    spaces = models.IntegerField(default=1)
    username = models.CharField(max_length=200, default='NONE')
    reservations = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    evac_reserved = models.TextField(default='NONE')
    dogAllowed = models.BooleanField(default=False)
    catAllowed = models.BooleanField(default=False)
    fishAllowed = models.BooleanField(default=False)
    birdAllowed = models.BooleanField(default=False)
    babyAllowed = models.BooleanField(default=False)
    kidAllowed = models.BooleanField(default=False)

    def get_address(self):
        return self.address

    def get_pets(self):
        return self.pets

    def get_spaces(self):
        return self.spaces

    def get_username(self):
        return self.username

    def get_reservations(self):
        return self.reservations

    def get_pub_date(self):
        return self.pub_date

    def get_evac_reserved(self):
        return self.evac_reserved

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def is_full(self):
        return self.spaces <= self.reservations

    def decrement_spaces(self, party):
        self.spaces = self.spaces - party
        return self.spaces

    @classmethod
    def create(cls, address, pets, spaces, username, dog, cat, fish, bird, baby, kid):
        location = EvacLocation(address=address, pets=pets,
                                spaces=spaces, username=username, reservations=0,
                                pub_date=timezone.now(), evac_reserved = 'NONE',
                                dogAllowed = dog, catAllowed = cat,
                                fishAllowed = fish, birdAllowed = bird,
                                babyAllowed = baby, kidAllowed = kid)
        return location

    @classmethod
    def areEqual(self, param_listing):
        areEqualBool = True
        if self.address != param_listing.get_address():
            areEqualBool = False
        if self.pets != param_listing.get_pets():
            areEqualBool = False
        if self.spaces != param_listing.get_spaces():
            areEqualBool = False
        if self.username != param_listing.get_username():
            areEqualBool = False
        if self.reservations != param_listing.get_reservations():
            areEqualBool = False
        if self.pub_date != param_listing.get_pub_date():
            areEqualBool = False
        return areEqualBool

    @classmethod
    def notDuplicateEvacuee(self, param_reserving_evacuee):
        if param_reserving_evacuee not in self.get_evac_reserved():
            return True
        else:
            return False

    @classmethod
    def append_evac_reserved(self, param_username):
        if self.evac_reserved == 'NONE':
            self.evac_reserved = param_username
        else:
            self.evac_reserved += param_username

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
