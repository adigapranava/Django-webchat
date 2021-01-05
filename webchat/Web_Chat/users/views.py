from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from chat.models import Messages

# queue = []

# Create your views here.
def register(request):
    if request.method == "POST":
        if request.POST["password1"]==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'users/register.html', {'error': "Username already exists"})
            except ObjectDoesNotExist:
                usr = User.objects.create_user(username= request.POST['username'],password= request.POST['password1'], email= request.POST['email'])
                #creating_a_profile_for_the_user
                pro = Profile(user = usr)
                pro.save()
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('login')
        else:
            return render(request, 'users/register.html', {'error': "Password Didn't Match"})
    else:   
        return render(request, 'users/register.html')


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], 
        password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'Logged in successfully')
            return redirect('chat-home')
        else:
            return render(request, 'users/login.html', {'error': "Invalid Login credientials."})
    else:
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('chat-home')