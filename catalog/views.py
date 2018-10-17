from django.shortcuts import render
from .models import Recept, Subscriptions, Article, Kind, Kitchen
from .forms import SubscribeForm, SendMessageFrom
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.syndication.views import Feed
from django.utils.encoding import iri_to_uri

class viewIndex(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        last3recepts = Recept.objects.all()[:3]
        last3Articles = Article.objects.all()[:2]
        ctx = {
            'last3_recept': last3recepts,
            'last3_articles': last3Articles,
            'last6_recept':Recept.objects.all().order_by('-current_date')[:6]
        }

        return render(request, self.template_name, ctx)

class ReceiptsListView(ListView):
    model = Recept
    paginate_by = 6

    def get_queryset(self):
        return Recept.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReceiptsListView, self).get_context_data(**kwargs)
        context['kind_query_set'] = Kind.objects.all()
        context['kitchen_query_set'] = Kitchen.objects.all().order_by('kitchen')
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
        print(request.POST)
        if query:
            search_query_set = Recept.objects.filter(title__icontains=query)
            if search_query_set:
                ctx = {'recept_list': search_query_set,
                       'kind_query_set': Kind.objects.all(),
                       'kitchen_query_set': Kitchen.objects.all()
                       }
                return render(request, self.template_name, context=ctx)
            else:
                ctx = {'kind_query_set': Kind.objects.all(),
                       'kitchen_query_set': Kitchen.objects.all()
                       }
                return render(request, self.template_name, context=ctx)
        elif request.POST.getlist('select1'):
            formList = request.POST.getlist('select1')
            if formList[0] and formList[1]:
                search_query_set = Recept.objects.filter(kind__kind__icontains=formList[0], kitchen__kitchen__icontains=formList[1])
                if search_query_set:
                    ctx = {'recept_list': search_query_set,
                           'kind_query_set': Kind.objects.all(),
                           'kitchen_query_set': Kitchen.objects.all()
                           }
                    return render(request, self.template_name, context=ctx)
            if formList[0] or formList[1]:
                search_query_set = Recept.objects.filter(kind__kind__icontains=formList[0]) if formList[0] else Recept.objects.filter(kitchen__kitchen__icontains=formList[1])
                if search_query_set:
                    ctx = {'recept_list': search_query_set,
                           'kind_query_set': Kind.objects.all(),
                           'kitchen_query_set': Kitchen.objects.all()
                           }
                    return render(request, self.template_name, context=ctx)
            ctx = {'kind_query_set': Kind.objects.all(),
                   'kitchen_query_set': Kitchen.objects.all(),
                   }
            return render(request, self.template_name, context=ctx)
        else:
            return render(request, self.template_name)


class Articles(ListView):
    model = Article
    paginate_by = 2

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

    def post(self, request, *args, **kwargs):
        form = SendMessageFrom(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            messages.success(request, 'Спасибо за отзыв! Это очень важно для нас!')
        else:messages.error(request, 'Не удалось отправить сообщение...попробуйте позже :(')
        return render(request, self.template_name)

class ReceptArticleFeed(Feed):
    title = "Perfect cooking - Отборные рецепты для вас"
    description = "Последние рецепты с сайта Perfect Cooking"
    link = 'feed/'

    def items(self):
        return Recept.objects.all().order_by('-current_date')

    def item_description(self, item):
        return item.text[:400]

    def item_title(self, item):
        return item.title