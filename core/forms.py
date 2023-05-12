from django import forms
from core import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Signup(forms.ModelForm):
    class Meta:
        model = models.post
        fields = ['firstname', 'lastname', 'email', 'password', 'confirmPassword']

