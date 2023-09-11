from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,AddItemForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count
from .models import UserProfile,Items


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
                return redirect('home')  
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
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

@login_required
def user_items(request):
    query = request.GET.get('query')
    user_profile = UserProfile.objects.filter(username=query).first()
      
    if user_profile:
        user_items = Items.objects.filter(user_profile=user_profile)
    else:
        user_items=None
    return render(request, 'user_page.html', {'user_items':user_items, 'query': query})

@login_required
def multiple_posts(request):
    query = request.GET.get("search_all")
    users_with_multiple_items = UserProfile.objects.annotate(item_count=Count('items')).filter(item_count__gt=1)

    return render(request,'user_page.html',{'users_with_multiple_items':users_with_multiple_items, 'query':query})
    
@login_required
def user_settings(request):
    return render(request,'user_settings.html')

@login_required
def my_items(request):
    user = UserProfile.objects.filter(username=request.user).first()
    if user:
        user_items = Items.objects.filter(user_profile=user)
    else:
        user_items = None
    return render(request, 'user_page.html',{'user_items':user_items})

@login_required
def delete_profile(request):
    if request.method =="POST":
        action_type = request.POST.get('action')
        if action_type == 'confirm':
            user = request.user
            user_profile = UserProfile.objects.get(username=user)
            user_profile.delete()
            logout(request)
            return redirect('home')
        else:
            return redirect('user_settings')
    return render(request,'user_settings.html')