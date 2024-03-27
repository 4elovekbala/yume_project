from rest_framework import serializers
from .models import Order, OrderProduct, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'start_date', 'end_date', 'total_cost', 'products']


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()

    class Meta:
        model = OrderProduct
        fields = ['product', 'order', 'rental_price', 'rental_duration']
