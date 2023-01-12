from django.db import models
from orders.models import Order
from products.models import Product

# Create your models here.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cake_flavor = models.CharField(max_length=100, default ="")
    frosting = models.CharField(max_length=100, default ="" )
    filling = models.CharField(max_length=100, default ="")
    design_details = models.TextField()
    price = models.IntegerField(default=0)