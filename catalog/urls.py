from django.conf.urls import url
from django.urls import path
from . import views
from .views import viewIndex, viewReceptSearch, ReceiptsListView, ReceiptDetailView


urlpatterns = [
    path('', viewIndex.as_view() , name='index'),
    path('index/', viewIndex.as_view() , name='index'),
    path('contact/', views.contact, name='contact'),
    path('receipe-search/', viewReceptSearch.as_view(), name='receipt search'),
    path('receipts/', ReceiptsListView.as_view(), name='receipt search'),
    url(r'^receipt/(?P<pk>.*)', views.ReceiptDetailView.as_view(), name='receipt-detail'),
    path('about/', views.about, name='about')
]