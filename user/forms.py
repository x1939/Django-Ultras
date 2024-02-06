from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
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
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image']

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if old_password and not self.instance.check_password(old_password):
            raise forms.ValidationError("Incorrect old password.")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")

        if old_password:
            raise forms.ValidationError("Old password is not allowed for profile update.")