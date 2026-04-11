from django.contrib import admin

# Register your models here.

from django.contrib import admin
from apps.product.models import Category, ModelProduct, Product
from apps.product.models import ProductImage

admin.site.register(Category)
admin.site.register(ModelProduct)
admin.site.register(Product)
admin.site.register(ProductImage)

