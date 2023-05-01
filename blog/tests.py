from django.urls import resolve
from django.test import TestCase
from blog.views import home_page
from blog.models import Article
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>Сайт Блог!</title>', html)
        self.assertIn('<h1>Денис</h1>', html)
        self.assertTrue(html.endswith('</html>'))


class ArticleModelTest(TestCase):
    
    def test_article_model_save_and_retrieve(self):
        article1 = Article(
            title='article 1',
            full_text='full_text',
            summary='summary 1',
            category='category 1',
            pubdate='pubdate 1',
        )
        article1.save()
        
        article2 = Article(
            title='article 2',
            full_text='full_text',
            summary='summary 2',
            category='category 2',
            pubdate='pubdate 2',
        )
        
        article2.save()

        all_articles = Article.objects.all()
        
        self.assertEqual(len(all_articles), 2)

        self.assertEqual(
            all_articles[0].title,
            article1.title
        )

        self.assertEqual(
            all_articles[1].title,
            article2.title
        )