from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    Productcs = Product.objects.all()
    context = {
        'title': 'Home',
        'products': Productcs
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'contact.html', context)

def shop(request):
    context = {
        'title': 'Shop',
    }
    return render(request, 'shop.html', context)

def styles(request):
    context = {
        'title': 'Styles',
    }
    return render(request, 'styles.html', context)

def thank_you(request):
    context = {
        'title': 'Thank You',
    }
    return render(request, 'thank-you.html', context)

def blog(request):
    context = {
        'title': 'Blog',
    }
    return render(request, 'blog.html', context)

def single_product(request, slug):
    Products = get_object_or_404(Product, slug=slug)

    context = {
        'title': Products.title,
        'product': Products,
    }
    return render(request, 'single-product.html', context)