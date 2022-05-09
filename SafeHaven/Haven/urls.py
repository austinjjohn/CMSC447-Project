from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user', views.login_user, name='login'),
    path('signup', views.signup, name='signup'),
    path('listings', views.listings, name='listings'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('evacuee', views.evacuee, name='evacuee'),
    path('map', views.map, name='map'),
]