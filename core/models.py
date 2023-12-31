from user.models import CustomUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.db.models import Min, Max
from datetime import datetime
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

class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0
    )
    likes = models.ManyToManyField(CustomUser, related_name='liked_products', blank=True)

    @property
    def discounted_price(self):
        discount_amount = (self.discount / 100) * self.price
        discounted_price = self.price - discount_amount
        return round(discounted_price, 2)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now()
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return self.name