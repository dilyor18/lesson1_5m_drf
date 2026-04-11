from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.product.views import (
    ProductViewSet
)

router = DefaultRouter()
router.register("product", ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    
]

urlpatterns += router.urls


