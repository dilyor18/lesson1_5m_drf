from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from apps.product.models import Product
from apps.product.serializers import (
    ProductCreateSerializer, ProductDetailSerializer,
    ProductSerializer
)

from apps.custom_pagination import CustomPagination
from apps.custom_filters import ProductFilter


class ProductViewSet(
    GenericViewSet,  
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        return Product.objects.select_related("category", "model")\
            .prefetch_related("images")\
            .order_by("-created_at")

    def get_serializer_class(self):
        if self.action == "create":
            return ProductCreateSerializer
        elif self.action == "retrieve":
            return ProductDetailSerializer
        return ProductSerializer

    def get_permissions(self):
        if self.action in ["create", "retrieve"]:
            return [IsAuthenticated()]
        return [AllowAny()]
