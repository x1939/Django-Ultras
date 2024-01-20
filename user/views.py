# yourapp/views.py
from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserProfileUpdateForm


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
    # Create a new instance of the UserProfileUpdateForm with the user's data
    form = UserProfileUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        if form.is_valid():
            user = form.save(commit=False)  # Don't save the form to the database yet

            if old_password and new_password:
                # Manually change the password
                if user.check_password(old_password):
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)  # Important for security
                    messages.success(request, 'Profile and password updated successfully.')
                else:
                    messages.error(request, 'Incorrect old password. Password not changed.')
            else:
                form.save()
                messages.success(request, 'Profile updated successfully.')

            return redirect('user-profile')

    return render(request, 'user-profile.html', {'form': form})