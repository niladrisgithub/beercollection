from django.shortcuts import render
from .models import Beer


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beers_index(request):
    beers = Beer.objects.all().order_by('-abv')
    return render(request, 'beers/index.html', {'beers': beers})