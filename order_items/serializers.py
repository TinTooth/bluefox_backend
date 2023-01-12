from rest_framework import serializers
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','order','product', 'quantity','design_details','frosting', 'filling','cake_flavor','price']
        depth = 1


class OrderItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order_id','product_id', 'quantity','design_details','frosting', 'filling','cake_flavor','price']

    order_id = serializers.IntegerField(write_only = True)
    product_id = serializers.IntegerField(write_only = True)
