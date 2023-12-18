from django.contrib.auth.models import User
from dajngo.contrib.auth.forms import UserCreationFrom
from django import forms

class User_Register(UserCreationFrom):

    class=Meta:
        model=User
        fields=['username','email','password1','pasword2']