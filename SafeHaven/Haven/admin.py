from django.contrib import admin

# Register your models here.
from .models import EvacLocation, Volunteer, Evacuee

admin.site.register(EvacLocation)

admin.site.register(Volunteer)

admin.site.register(Evacuee)
