from django.db import models

# Create your models here.

class Payment(models.Model):
    order_id = models.CharField(max_length=200)
    product_name = models.CharField(max_length=50)
    product_amount = models.CharField(max_length=50)
    created_at = models.CharField(max_length=100)
