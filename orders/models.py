from django.db import models
from authentication.models import User

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length = 120)
    customer_phone_number= models.CharField(max_length = 120)
    customer_email = models.EmailField(max_length = 120,default='none')
    deliver_date = models.DateField()
    status = models.CharField(max_length=32)
    total_price = models.FloatField()
    total_work_time = models.FloatField()
    notes = models.TextField()
    adjusted_price = models.FloatField(default = 0)
