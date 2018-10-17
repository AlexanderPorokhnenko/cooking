from django.test import TestCase
from catalog.models import Article, Recept
from django.urls import reverse


class ArticleListViewTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        number_of_articles = 100
        for article_num in range(number_of_articles):
            Article.objects.create(title='Article %s' % article_num, tags='Tags %s' % article_num, text='TextTextText %s' % article_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/articles/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('articles'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('articles'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalog/article_list.html')

    def test_pagination_is_2(self):
        resp = self.client.get(reverse('articles'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertEqual(len(resp.context['article_list']), 2)

    def test_lists_all_articles(self):
        resp = self.client.get(reverse('articles')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue( len(resp.context['article_list']) == 2)


class ReceiptListViewTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        number_of_recepts = 100
        for recept_num in range(number_of_recepts):
            Recept.objects.create(title='receipt %s' % recept_num, tags='Tags %s' % recept_num, text='TextTextText %s' % recept_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/receipts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('receipt search'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('receipt search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'catalog/recept_list.html')

    def test_pagination_is_6(self):
        resp = self.client.get(reverse('receipt search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertEqual(len(resp.context['recept_list']), 6)

    def test_lists_all_receipts(self):
        resp = self.client.get(reverse('receipt search')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['recept_list']) == 6)