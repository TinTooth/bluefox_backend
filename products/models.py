from django.db import models

# Create your models here.
class Product(models.Model):
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=32)
    work_time = models.FloatField()
    description = models.TextField()
    pricebydozen = models.BooleanField(default=False)
