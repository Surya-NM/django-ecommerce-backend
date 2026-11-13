from rest_framework import serializers
from .models import cart, cartItem


class CartItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source='product.name',
        read_only=True
    )

    product_price = serializers.DecimalField(
        source='product.price',
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = cartItem
        fields = [
            'id',
            'product_name',
            'product_price',
            'quantity',
            'product',
            'total_price'
        ]

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity


class CartSerilaizer(serializers.ModelSerializer):

    items = CartItemSerializer(
        source='Items',
        many=True,
        read_only=True
    )

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = cart
        fields = [
            'id',
            'items',
            'total_price',
            'created_at',
            'updated_at'
        ]

    def get_total_price(self, obj):

        total = 0

        for item in obj.Items.all():
            total += item.product.price * item.quantity

        return total