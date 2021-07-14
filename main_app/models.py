from django.db import models
from django.urls import reverse

# Create your models here.

SERVED = (
    ('C', 'Can'),
    ('B', 'Bottle'),
    ('D', 'Draft'),
    ('G', 'Growler'),
)

class Venue(models.Model):
    name = models.CharField(max_length=25, default='')
    address = models.CharField(max_length=45, default='')
    city = models.CharField(max_length=30, default='')
    state = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'venue_id': self.id})



class Hop(models.Model):
    name = models.CharField(max_length=15, default='')
    characteristics = models.CharField(max_length=170, default='')
    alpha_acid = models.DecimalField(max_digits=5, decimal_places=2, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'hop_id': self.id})



class Beer(models.Model):
    brewery_name = models.CharField(max_length=100)
    beer_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    type = models.CharField(max_length=15)
    abv = models.DecimalField(max_digits=5, decimal_places=2)
    # add M:M relationship
    hops = models.ManyToManyField(Hop)
    venues = models.ManyToManyField(Venue)

    def __str__(self):
        return(self.beer_name)
  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'beer_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for beer_id: {self.beer_id} @{self.url}"

class Drinking(models.Model):
    class Meta:
        ordering = ['-date']
    
    date = models.DateField('drinking date')
    served = models.CharField(
        max_length=1,
        choices=SERVED,
        default=SERVED[0][0]
    )

    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_served_display()} on {self.date}"

