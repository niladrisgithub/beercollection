from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beers/', views.beers_index, name='index'),
    path('beers/<int:beer_id>/add_drinking', views.add_drinking, name='add_drinking'),
    path('beers/<int:beer_id>/', views.beers_detail, name='detail'),
    path('beers/create/', views.BeerCreate.as_view(), name='beers_create'),
    path('beers/<int:pk>/update/', views.BeerUpdate.as_view(), name='beers_update'),
    path('beers/<int:pk>/delete/', views.BeerDelete.as_view(), name='beers_delete'),
    path('beers/<int:beer_id>/assoc_hop/<int:hop_id>/', views.assoc_hop, name='assoc_hop'),
    path('hops/', views.hops_index, name='hops_index'),
    path('hops/<int:hop_id>/', views.hops_detail, name='hops_detail'),
    path('hops/create/', views.HopsCreate.as_view(), name='hops_create'),
    path('hops/<int:pk>/update/', views.HopsUpdate.as_view(), name='hops_update'),
    path('hops/<int:pk>/delete/', views.HopsDelete.as_view(), name='hops_delete'),
]