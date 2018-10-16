from django.conf.urls import url
from django.urls import path
from . import views
from .views import viewIndex, viewReceptSearch, ReceiptsListView, Search, Articles, ReceptArticleFeed, AboutView

urlpatterns = [
    path('', viewIndex.as_view() , name='index'),
    path('index/', viewIndex.as_view() , name='index'),
    path('receipe-search/', viewReceptSearch.as_view(), name='receipt search'),
    path('receipts/', ReceiptsListView.as_view(), name='receipt search'),
    url(r'^receipt/(?P<pk>.*)', views.ReceiptDetailView.as_view(), name='receipt-detail'),
    url(r'^article/(?P<pk>.*)', views.ArticlesDetail.as_view(), name='article-detail'),
    path('about/', AboutView.as_view(), name='about'),
    url(r'subscribe/', views.subscribe, name='subscribe_form'),
    url(r'receiptSearch/', Search.as_view(), name='search_form'),
    url(r'articles/', Articles.as_view(), name='articles'),
    url(r'^feed/$', views.ReceptArticleFeed()),
]