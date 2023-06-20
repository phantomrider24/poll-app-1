from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class User_Register_Form(UserCreationForm):
    first_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username','password1','first_name')

