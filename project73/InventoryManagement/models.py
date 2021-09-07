from django.db import models

# Create your models here.

class Product(models.Model):
    date=models.DateField()
    provider=models.CharField(max_length=50)
    name_of_product=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    amount=models.IntegerField()
    stock=models.IntegerField()

    
