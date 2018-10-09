from django.shortcuts import render
from .models import Kitchen, Kind, Recept
from django.views.generic import TemplateView, ListView, DetailView

class viewIndex(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        last3receptsTitles = Recept.objects.all().values()[:3]
        ctx = {
            'recept_titles': last3receptsTitles
        }

        return render(request, self.template_name, ctx)

class ReceiptsListView(ListView):
    model = Recept

    def get_queryset(self):
        return Recept.objects.all()[:3]

    def get_context_data(self, **kwargs):
        context = super(ReceiptsListView, self).get_context_data(**kwargs)
        return context

class ReceiptDetailView(DetailView):
    model = Recept

class viewReceptSearch(TemplateView):

    template_name = 'receipe-post.html'
    def get(self, request, *args, **kwargs):
        ctx = {Recept.objects.all()}
        return render(request, self.template_name)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
