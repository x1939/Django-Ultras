from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from .forms import *


def home(request):
    products = Product.objects.all()
    blogs = Blog.objects.all()

    context = {
        'title': 'Home',
        'products': products,
        'blogs': blogs,
    }
    return render(request, 'home.html', context)

def about(request):
    blogs = Blog.objects.all()
    context = {
        'title': 'About',
        'blogs': blogs,
    }
    return render(request, 'about.html', context)

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user if request.user.is_authenticated else None)
        if form.is_valid():
            form.save()
            return redirect('thank-you')  # Redirect to a success page or any other page
    else:
        form = ContactForm(user=request.user if request.user.is_authenticated else None)

    return render(request, 'contact.html', {'form': form, 'title': 'Contact'})

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    blogs = Blog.objects.all()

    selected_category_title = request.GET.get('category', None)
    selected_brand_name = request.GET.get('brand', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    search_query = request.GET.get('search', None)

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

    # Filter products based on the search query (product title)
    if search_query:
        products = products.filter(Q(title__icontains=search_query))

    # Pagination
    paginator = Paginator(products, 8)  # Show 10 products per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'title': 'Shop',
        'products': products,
        'categories': categories,
        'brands': brands,
        'blogs': blogs,
        'selected_category': selected_category,
        'selected_brand': selected_brand,
        'min_price': min_price,
        'max_price': max_price,
        'search_query': search_query,
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
    blogs = Blog.objects.all()
    context = {
        'title': 'Blog',
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)

@login_required
def single_product(request, slug):
    products = get_object_or_404(Product, slug=slug)

    context = {
        'title': products.title,
        'product': products,
    }
    return render(request, 'single-product.html', context)

def single_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Assuming you have user authentication
            comment.blog = blog
            comment.save()
            return redirect('single-blog', slug=slug)
    else:
        form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
        'title': blog.title,
    }

    return render(request, 'single-blog.html', context)

@login_required
def like_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.user in product.likes.all():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)

    return redirect('home')
