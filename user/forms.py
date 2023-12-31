from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.ImageField(required=False)  # Use required=False if the image is not mandatory

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image', 'password1', 'password2']
