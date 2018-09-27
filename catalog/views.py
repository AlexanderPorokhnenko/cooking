from django.shortcuts import render
from .models import Kitchen, Kind, Recept

def index(request):
    num_recept = Recept.objects.all().count(),
    recept_title = Recept.objects.all()
    last3recepts = Recept.objects.all().values()
    print(last3recepts)
    return render(request,'index.html', context={'num_recepts':num_recept, 'recept_titles':last3recepts})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
