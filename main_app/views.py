from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect, render
from .models import Beer, Hop
from .forms import DrinkingForm


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

def beers_detail(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    drinking_form = DrinkingForm()
    return render(request, 'beers/detail.html', {
        'beer': beer,
        'drinking_form': drinking_form
        })

def assoc_hop(request, beer_id, hop_id):
    Beer.objects.get(id=beer_id).hops.add(hop_id)
    return redirect('detail', beer_id=beer_id)

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
