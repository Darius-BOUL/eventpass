from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    is_organizer = forms.BooleanField(required=False, label="Je suis organisateur")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_organizer', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
