from django.shortcuts import render
from .models import Kitchen, Kind, Recept
from django.db.models.functions import Substr
from django.views.generic import TemplateView

class viewIndex(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        last3receptsTitles = Recept.objects.all().values()[:3]
        for item in last3receptsTitles:
            print(item['title'])

        ctx = {
            'recept_titles': last3receptsTitles
        }

        return render(request, self.template_name, ctx)
# def index(request):
#     num_recept = Recept.objects.all().count(),
#     recept_title = Recept.objects.all()
#     last3recepts = Recept.objects.all().values()
#     print(not last3recepts.values('text').annotate(firsrsymb= Substr('text',1,50)))
#     return render(request,'index.html', context={'num_recepts':num_recept, 'recept_titles':last3recepts})
class viewReceptSearch(TemplateView):
    template_name = 'receipe-post.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
