from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer (serializers.ModelSerializer):
    product_name = serializers.CharField(
        source = 'Product.name',
        read_only = True
    )

    class Meta :
        model = OrderItem
        fields =[
            'id',
            'product',
            'product_name',
            'price',
            'total_price'
        ]

        read_only = [
            'price',
            'total_price'
        ]

class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "items",
            "total_price",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "user",
            "items",
            "total_price",
            "status",
            "created_at",
            "updated_at",
        ]
    