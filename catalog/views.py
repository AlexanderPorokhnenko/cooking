from django.shortcuts import render
from .models import Recept, Subscriptions, Article
from .forms import SubscribeForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

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
        return Recept.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReceiptsListView, self).get_context_data(**kwargs)
        return context

class ReceiptDetailView(DetailView):
    model = Recept

    def get_context_data(self, **kwargs):
        context = super(ReceiptDetailView, self).get_context_data(**kwargs)
        return context

    def get_context_data(self, **kwargs):
        context = super(ReceiptDetailView, self).get_context_data(**kwargs)
        return context


class viewReceptSearch(TemplateView):
    template_name = 'receipe-post.html'

    def get(self, request, *args, **kwargs):
        ctx = {Recept.objects.all()}
        return render(request, self.template_name)


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.cleaned_data.get('email')
            if form.cleaned_data.get('email') not in set(i['email'] for i in Subscriptions.objects.all().values('email')):
                form.save()
                messages.success(request, 'Поздравляем! Ваш email успешно подписан на рассылку!')
            else:
                messages.error(request, "Введенный email уже подписан на рассылку!")
            return HttpResponseRedirect(reverse('index'))

class Search(ListView):
    model = Recept
    template_name = 'catalog/recept_list.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('search')
        if query:
            search_query_set = Recept.objects.filter(title__icontains=query)
            if search_query_set:
                ctx = {'recept_list': search_query_set}
                return render(request, self.template_name, context=ctx)
            else:
                return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        query = request.POST.get('search')
        if query:
            search_query_set = Recept.objects.filter(title__icontains=query)
            if search_query_set:
                ctx = {'recept_list': search_query_set}
                return render(request, self.template_name, context=ctx)
            else:
                return render(request, self.template_name)


class Articles(ListView):
    model = Article

class ArticlesDetail(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticlesDetail, self).get_context_data(**kwargs)
        return context

    def get_context_data(self, **kwargs):
        context = super(ArticlesDetail, self).get_context_data(**kwargs)
        return context

class AboutView(TemplateView):
    template_name = 'about.html'
# def about(request):
#     return render(request, 'about.html')
