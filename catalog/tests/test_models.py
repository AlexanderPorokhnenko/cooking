from django.test import TestCase
from catalog.models import Article, Recept


class ArticleTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='Fresh potatos', text='blablablablabla', tags='a,b,c,d, e, f   , g')

    def test_article_title(self):
        article = Article.objects.all()[:1].get()
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_article_text(self):
        article = Article.objects.all()[:1].get()
        field_label = article._meta.get_field('text').verbose_name
        self.assertEquals(field_label,'text')

    def test_title_max_length(self):
        article = Article.objects.all()[:1].get()
        max_length = article._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_article_get_absoulte_url(self):
        article = Article.objects.all()[:1].get()
        self.assertEquals(article.get_absolute_url(), '/article/'+str(article.id))

    def test_article_split_tags(self):
        article = Article.objects.all()[:1].get()
        self.assertEquals(article.split_tags(), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])


class ModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recept.objects.create(title='Nice pasta', text='pasta is; amazing italian; food', tags='spaghetti, meat, milk, eggs   ,   italiano')

    def test_recept_title(self):
        recept = Recept.objects.all()[:1].get()
        field_label = recept._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_recept_text(self):
        recept = Recept.objects.all()[:1].get()
        field_label = recept._meta.get_field('text').verbose_name
        self.assertEquals(field_label,'text')

    def test_title_max_length(self):
        recept = Recept.objects.all()[:1].get()
        max_length = recept._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_receipt_get_absoulte_url(self):
        recept = Recept.objects.all()[:1].get()
        self.assertEquals(recept.get_absolute_url(), '/receipt/'+str(recept.id))

    def test_receipt_split_tags(self):
        recept = Recept.objects.all()[:1].get()
        self.assertEquals(recept.split_tags(), ['spaghetti', 'meat', 'milk', 'eggs', 'italiano'])

    def test_receipt_split_text(self):
        recept = Recept.objects.all()[:1].get()
        self.assertEquals(recept.split_text(), ['pasta is', 'amazing italian', 'food'])