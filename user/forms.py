from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ClearableFileInput
from .models import CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image', 'password1', 'password2']

class UserProfileUpdateForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput, required=False)
    new_password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image']

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if old_password and not self.instance.check_password(old_password):
            raise forms.ValidationError("Incorrect old password.")
        return old_password