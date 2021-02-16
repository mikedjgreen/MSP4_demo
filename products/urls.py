from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('', views.all_artworks, name='artworks')
]
