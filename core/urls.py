from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/<slug:slug>/', single_product, name='single-product'),
    path('blog/<slug:slug>/', single_blog, name='single-blog'),
    path('like/<int:product_id>/', like_product, name='like_product'),
    path('shop/', shop, name='shop'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('thankyou/', thank_you, name='thank-you'),
    path('add_to_basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
]