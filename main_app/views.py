from django.shortcuts import render


#TODO Temp Beer Class for testing purposes

class Beer():
    def __init__(self, brewery_name, beer_name, description, type, abv):
        self.brewery_name = brewery_name
        self.beer_name = beer_name
        self.description = description
        self.type = type
        self.abv = abv

beers = [
    Beer('Harpoon', 'Rec League', 'light, hoppy, low calorie, full of flavor', 'session IPA', 3.8),
    Beer('Tree House', 'Jjjuliusss', 'bold, citrusy', 'American IPA', 6.8),
    Beer('Allagash', 'Black', 'silky flavors of chocolate and coffee', 'stout', 7.5),
    Beer('Miller', 'High-Life', 'crisp and refreshing, just like you remember', 'American Lager', 4.6),
    Beer('Lagunitas', 'DayTime', 'hop-forward, light and refreshing, too easy to drink all day ', 'session IPA', 4)
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def beers_index(request):
    return render(request, 'beers/index.html', {'beers': beers})