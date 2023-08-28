from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,AddItemForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import UserProfile


def home(request):
    return render(request,'home.html')

def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('home') 
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})
    

def login_method(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                messages.success(request,"You have logged in successfully!")
                return redirect('home')  
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request,"You have logged out successfully!")

    return redirect('home')

@login_required
def add_item(request):
    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            user_profile = UserProfile.objects.get(username=request.user)
            item.user_profile = user_profile
            item.username=request.user.username
            item.save()
            return redirect('home')
    else:
        form = AddItemForm()
    return render(request,'user_page.html', {'form':form})

@login_required
def user_page(request):
    return render(request,'user_page.html')
        
