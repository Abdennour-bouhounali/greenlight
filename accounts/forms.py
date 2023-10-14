from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

from .models import User

INPUT_CLASSES = "rounded p-4 w-full bg-gray-200 text-gray-800 placeholder-gray-700 mb-5"

CHOICES = [
    ('donator', 'Donator'),
    ('deposit', 'Deposit'),
    ('volunteer', 'Volunteer'),
]

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Enter your username',
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Enter your password'
    }))

class UserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Enter a username',
    }))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Enter your email address',
    }))
    # account_type = forms.ChoiceField(choices=CHOICES, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Enter a password',
    }))
    password2 = forms.CharField(label='Confirm your password', widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES,
        'placeholder': 'Confirm the password',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email already exists")
        return self.cleaned_data
    
