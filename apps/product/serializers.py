from rest_framework import serializers

from apps.product.models import Category, ModelProduct, Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]

class ProductSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()
 
    class Meta:
        model = Product
        fields = [
            "id", "user", "uuid", "title", "description",
            "price", "first_image"
        ]

    def get_first_image(self, obj):
        first_img = obj.product_image.first()
        if first_img:
            return first_img.image.url
        return None

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True, source="product_image")
    category_title = serializers.SerializerMethodField()
    model_title = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id", "user", "uuid", "title", "description",
            "price", "is_active", "category_title",
            "model_title", "images"
        ]

    def get_category_title(self, obj):
        if obj.category:
            return obj.category.title
        return None

    def get_model_title(self, obj):
        if obj.model:
            return obj.model.title
        return None

class ProductCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True,
    )
    model = serializers.PrimaryKeyRelatedField(
        queryset=ModelProduct.objects.all(),
        required=False,
        allow_null=True,
    )
    price = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        model = Product
        fields = [
            "title", "description",
            "price", "category",
            "model", "images"
        ]

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Название должно быть минимум 3 символа!")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше 0!")
        return value

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])

        request = self.context.get("request")
        product = Product.objects.create(
            user=request.user,
            **validated_data
        )

        for img in images_data:
            ProductImage.objects.create(product=product, image=img)

        return product






