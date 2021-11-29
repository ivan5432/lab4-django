from django.test import TestCase
from django.urls import reverse,resolve

from .views import HomePageView, ArticleDetail

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)
    def test_category_view_status_code(self):
        url = reverse('articles-category-list',args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    def test_articles_list_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    def test_news_detail_url_resolves_news_detail_view(self):
        view = resolve('/articles/2021/11/18/cherven')
        self.assertEquals(view.func.view_class, ArticleDetail)
