from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "username"}))

    firstname = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields =['username','email']