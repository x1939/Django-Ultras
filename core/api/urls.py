from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', ContacList.as_view()),
    path('blog/', BlogList.as_view()),
    path('product/', ProductList.as_view()),
]