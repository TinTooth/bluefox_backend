from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','customer_email','customer_name','customer_phone_number','deliver_date','status', 'total_work_time','total_price','notes','adjusted_price']
        depth = 1