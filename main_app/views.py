from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect, render
from .models import Beer, Hop, Venue, Photo
from .forms import DrinkingForm

import boto3
import uuid

S3_BASE_URL = 'http://s3.us-east-1.amazonaws.com/'
BUCKET = 'nils-beer-collector'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beers_index(request):
    beers = Beer.objects.all().order_by('abv')
    return render(request, 'beers/index.html', {'beers': beers})

def add_drinking(request, beer_id):
    form = DrinkingForm(request.POST)
    if form.is_valid():
        new_drinking = form.save(commit=False)
        new_drinking.beer_id = beer_id
        new_drinking.save()
    return redirect('detail', beer_id=beer_id)

def add_photo(request, beer_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, beer_id=beer_id)
            photo.save()
        except Exception as error:
            print('An error occured uploading file to S3')
            print(error)
    return redirect('detail', beer_id=beer_id)            

def beers_detail(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    hops_beer_doesnt_have = Hop.objects.exclude(id__in = beer.hops.all().values_list('id'))
    venue_beer_doesnt_have = Venue.objects.exclude(id__in = beer.venues.all().values_list('id'))
    drinking_form = DrinkingForm()
    return render(request, 'beers/detail.html', {
        'beer': beer,
        'drinking_form': drinking_form,
        'hops': hops_beer_doesnt_have,
        'venues': venue_beer_doesnt_have,
        })

# def assoc_hop(request, beer_id, hop_id):
#     Beer.objects.get(id=beer_id).hops.add(hop_id)
#     return redirect('detail', beer_id=beer_id)

def assoc_hop(request, beer_id, hop_id):
    Beer.objects.get(id=beer_id).hops.add(hop_id)
    return redirect('detail', beer_id=beer_id)

def assoc_venue(request, beer_id, venue_id):
    Beer.objects.get(id=beer_id).venues.add(venue_id)
    return redirect('detail', beer_id=beer_id)

class BeerCreate(CreateView):
    model = Beer
    fields = ['brewery_name', 'beer_name', 'description', 'type', 'abv']
    success_url = '/beers/'

class BeerUpdate(UpdateView):
    model = Beer
    fields = ['description', 'type', 'abv']

class BeerDelete(DeleteView):
    model = Beer
    success_url = '/beers/'

def hops_index(request):
    hops = Hop.objects.all()
    return render(request, 'hops/index.html', {'hops': hops})

def hops_detail(request, hop_id):
    hop = Hop.objects.get(id=hop_id)
    return render(request, 'hops/detail.html', {'hop': hop})

class HopsCreate(CreateView):
    model = Hop
    fields = '__all__'
    success_url = '/hops/'

class HopsUpdate(UpdateView):
    model = Hop
    fields = ['characteristics', 'alpha_acid']

class HopsDelete(DeleteView):
    model = Hop
    success_url = '/hops/'


def venues_index(request):
    venue = Venue.objects.all()
    return render(request, 'venues/index.html', {'venue': venue})

def venue_detail(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    return render(request, 'venues/detail.html', {'venue': venue})

class VenueCreate(CreateView):
    model = Venue
    fields = '__all__'
    success_url = '/venues/'

class VenueUpdate(UpdateView):
    model = Venue
    fields = ['address', 'city', 'state']
    success_url = '/venues/'

class VenueDelete(DeleteView):
    model = Venue
    success_url = '/venues/'

