from django.db import models
from django.urls import reverse

# Create your models here.

class Beer(models.Model):
    brewery_name = models.CharField(max_length=100)
    beer_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    type = models.CharField(max_length=15)
    abv = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return(self.beer_name)
  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'beer_id': self.id})


class Hops(models.Model):
    name: models.CharField(max_length=20)
    characteristics: models.CharField(max_length=50)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'hop_id': self.id})