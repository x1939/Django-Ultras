# yourapp/urls.py
from django.urls import path
from .views import register, user_login, user_logout, user_profile

urlpatterns = [
    path('register/', register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('profile/', user_profile, name='user-profile'),
]