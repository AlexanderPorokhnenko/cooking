from django.conf.urls import url
from django.urls import path
from . import views
from .views import viewIndex, viewReceptSearch


urlpatterns = [
    path('', viewIndex.as_view() , name='index'),
    path('index/', viewIndex.as_view() , name='index'),
    path('contact/', views.contact, name='contact'),
    path('receipe-search/', viewReceptSearch.as_view(), name='receipt search'),
    path('about/', views.about, name='about')
]