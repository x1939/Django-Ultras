from user.models import CustomUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone
from ckeditor.fields import RichTextField

CustomUser = get_user_model()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'

class Brand(BaseModel):
    title = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

class ProductManager(models.Manager):
    def filter_by_price(self, products, min_price=None, max_price=None):
        if min_price is not None and max_price is not None:
            return products.filter(price__range=(min_price, max_price))
        return products

class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True, null=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_products', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    objects = ProductManager()

    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0
    )

    @property
    def discounted_price(self):
        discount_amount = (self.discount / 100) * self.price
        discounted_price = self.price - discount_amount
        return round(discounted_price, 2)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Information(models.Model):
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email
    
class Logo(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Blog(models.Model):

    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Auto-generate slug from the title
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        if self.user:
            return f"Contact by {self.user.username} - {self.name}"
        else:
            return f"Contact - {self.name} (No associated user)"
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"
