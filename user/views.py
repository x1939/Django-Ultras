import logging
from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserProfileUpdateForm

# Use Django's built-in logger
logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change 'home' to your desired URL
        else:
            # Form is not valid, display error messages
            messages.error(request, 'There are errors in the form. Please correct them.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Change 'home' to your desired URL
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  # Change 'home' to your desired URL

@login_required
def user_profile(request):
    user = request.user
    form = UserProfileUpdateForm(instance=user)
    password_form = PasswordChangeForm(user, request.POST)

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user)

        if 'old_password' not in request.POST or 'new_password1' not in request.POST or 'new_password2' not in request.POST:
            # Process profile update only if password change fields are not present
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully.')
                logger.info(f'User {user.username} updated profile successfully.')
                return redirect('user-profile')

        else:
            # Process password change only if password change fields are present
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                if user.check_password(password_form.cleaned_data['old_password']):
                    user.set_password(password_form.cleaned_data['new_password1'])
                    user.save()
                    update_session_auth_hash(request, user)  # Important for security
                    messages.success(request, 'Password changed successfully.')
                    logger.info(f'User {user.username} changed password successfully.')
                    return redirect('user-profile')
                else:
                    messages.error(request, 'Incorrect current password.')
                    return redirect('user-profile')
            else:
                print("Password form is not valid.")
                print(password_form.errors)
                messages.error(request, 'Invalid password change request.')
                return redirect('user-profile')

    return render(request, 'user-profile.html', {'form': form, 'password_form': password_form})