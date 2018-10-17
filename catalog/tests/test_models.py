from django.test import TestCase
from catalog.models import Article

class ArticleTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='Fresh potatos', text='blablablablabla', tags='a,b,c,d, e, f   , g')

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

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

