from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    is_organizer = forms.BooleanField(required=False, label="Je suis organisateur")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_organizer', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': "Nom d'utilisateur",
            'class': "form-control"
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': "Mot de passe",
            'class': "form-control"
        })

