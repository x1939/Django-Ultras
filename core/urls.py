from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/<slug:slug>/', single_product, name='single-product'),
    path('shop/', shop, name='shop'),
    path('blog/', blog, name='blog'),
    path('styles/', styles, name='styles'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('thankyou/', thank_you, name='thank-you'),
]