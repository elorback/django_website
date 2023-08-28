from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,Items

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email']

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['title','description', 'price']

