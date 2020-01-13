from django.db import models

# Create your models here.
from django.db import models
class Category(models.Model):
    """Tag to be used for a objective"""
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """Tag to be used for a objective"""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    listed_price = models.FloatField(default = 0)	
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    