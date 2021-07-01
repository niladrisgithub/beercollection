from django.db import models

# Create your models here.

class Beer(models.Model):
    brewery_name = models.CharField(max_length=100)
    beer_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    type = models.CharField(max_length=15)
    abv = models.DecimalField(max_digits=5, decimal_places=2)


  