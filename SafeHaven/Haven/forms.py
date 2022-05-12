from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterationForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=30)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

        # def clean(self):
        #     cleaned_data = super().clean()
        #     password1 = self.cleaned_data.get('password1')
        #     password2 = self.cleaned_data.get('password2')
        #
        #     if User.objects.filter(username = cleaned_data["username"]).exists():
