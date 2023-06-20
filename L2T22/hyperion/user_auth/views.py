from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import User_Register_Form 

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html',{
        "username": request.user.username,
        "password": request.user.password
    })

def authenticate_user(request):
    username = request.POST['username']
    password= request.POST['password']
    user = authenticate(username=username, password = password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request,user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )
    
def register_user(request):
    if request.method == "POST":
        form = User_Register_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password = password) 
            messages.success(request,("Registration completed"))
            return HttpResponseRedirect(
                reverse('user_auth:show_user')
            )
    else:
        form = User_Register_Form()
    return render(request, 'authentication/user_registration.html',{
        'form':form,
    })
