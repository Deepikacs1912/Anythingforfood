from dataclasses import field
from socket import fromshare
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['email','password1','password2']