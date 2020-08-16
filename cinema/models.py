from django.db import models

# Create your models here.

class Cinema(models.Model):
    city = models.CharField(max_length = 100)
    name = models.CharField(max_length = 200)
    adress = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 16)

class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    number = models.IntegerField()

class Pricing(models.Model):
    priceNor = models.DecimalField(decimal_places=2, max_digits=5)
    priceSch = models.DecimalField(decimal_places=2, max_digits=5)
    priceStud = models.DecimalField(decimal_places=2, max_digits=5)
    priceChild = models.DecimalField(decimal_places=2, max_digits=5)
    priceName = models.CharField(max_length=40)

class Place(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row = models.IntegerField()
    number = models.IntegerField()
