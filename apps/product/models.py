from django.db import models

# Create your models here.

from django.db import models
from apps.user.models import User
import uuid

class Category(models.Model):
    title = models.CharField(
        max_length=155,
    )
    image = models.ImageField(
        upload_to='category'
    )

    def __str__(self):
        return self.title

class ModelProduct(models.Model):
    title = models.CharField(
        max_length=155,
    )
    image = models.ImageField(
        upload_to='category'
    )

    def __str__(self):
        return self.title

class Product(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_product"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name="category_product",
        blank=True, null=True
    )
    model = models.ForeignKey(
        ModelProduct, on_delete=models.CASCADE,
        related_name="model_product",
        blank=True, null=True
    )
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    title = models.CharField(
        max_length=255
    )
    description = models.TextField()
    price = models.CharField(
        max_length=15
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='product'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_image'
    )



