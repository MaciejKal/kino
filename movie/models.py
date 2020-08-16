from django.db import models
from cinema import models as cinema

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    image = models.ImageField()

class Preview(models.Model):
    cinema = models.ForeignKey(cinema.Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    premiere = models.DateField()

class Show(models.Model):
    cinema = models.ForeignKey(cinema.Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    dateFrom = models.DateField()
    dateTo = models.DateField()

class ShowHall(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    hall = models.ForeignKey(cinema.Hall, on_delete=models.CASCADE)
    pricing = models.ForeignKey(cinema.Pricing, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()

class Reservation(models.Model):
    showHall = models.ForeignKey(ShowHall, on_delete=models.CASCADE)
    place = models.ForeignKey(cinema.Place, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    payed = models.BooleanField()
    mail = models.CharField(max_length=100)
    ukey = models.BooleanField()

