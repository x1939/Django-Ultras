from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *


def home(request):
    products = Product.objects.all()

    context = {
        'title': 'Home',
        'products': products,
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
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    selected_category_title = request.GET.get('category', None)
    selected_brand_name = request.GET.get('brand', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)

    # Filter products based on the selected category title
    if selected_category_title:
        if selected_category_title.lower() == 'all':
            selected_category = None
        else:
            selected_category = get_object_or_404(Category, title=selected_category_title)
            products = products.filter(category=selected_category)
    else:
        selected_category = None

    # Filter products based on the selected brand name
    if selected_brand_name:
        if selected_brand_name.lower() == 'all':
            selected_brand = None
        else:
            selected_brand = get_object_or_404(Brand, title=selected_brand_name)
            products = products.filter(brand=selected_brand)
    else:
        selected_brand = None

    # Filter products based on price range
    if min_price is not None and max_price is not None:
        products = products.filter(price__range=(min_price, max_price))

    context = {
        'title': 'Shop',
        'products': products,
        'categories': categories,
        'brands': brands,
        'selected_category': selected_category,
        'selected_brand': selected_brand,
        'min_price': min_price,
        'max_price': max_price,
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
    products = get_object_or_404(Product, slug=slug)

    context = {
        'title': products.title,
        'product': products,
    }
    return render(request, 'single-product.html', context)

def like_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.user in product.likes.all():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)

    return redirect('home')