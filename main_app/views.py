from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render
from .models import Beer, Hop


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beers_index(request):
    beers = Beer.objects.all().order_by('abv')
    return render(request, 'beers/index.html', {'beers': beers})

def beers_detail(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    return render(request, 'beers/detail.html', {'beer': beer})

class BeerCreate(CreateView):
    model = Beer
    fields = '__all__'
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
