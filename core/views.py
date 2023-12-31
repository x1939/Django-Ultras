from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()

            return redirect('thank-you')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

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

def like_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if the custom user has already liked the product
    if request.user in product.likes.all():
        # User has already liked, unlike the product
        product.likes.remove(request.user)
    else:
        # User hasn't liked, like the product
        product.likes.add(request.user)

    return redirect('home')