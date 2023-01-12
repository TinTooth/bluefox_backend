from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user','deliver_date','status', 'total_work_time','total_price','notes','adjusted_price']
        depth = 1