from django import forms
from .models import Contact_us_page
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
class ProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            )
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

class User_Login(AuthenticationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput())

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_us_page
        fields = ['name', 'email']
