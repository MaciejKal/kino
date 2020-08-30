from django.db import models

# Create your models here.

class Cinema(models.Model):
    city = models.CharField(max_length = 100)
    name = models.CharField(max_length = 200)
    adress = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 16)

    def __str__(self):
        return self.name

class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return self.cinema.name + ' sala:' + self.number.__str__()

class Pricing(models.Model):
    priceNor = models.DecimalField(decimal_places=2, max_digits=5)
    priceSch = models.DecimalField(decimal_places=2, max_digits=5)
    priceStud = models.DecimalField(decimal_places=2, max_digits=5)
    priceChild = models.DecimalField(decimal_places=2, max_digits=5)
    priceName = models.CharField(max_length=40)
    priceType = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.priceName

class Place(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.hall.cinema.name + ' sala:' + self.hall.number.__str__()
