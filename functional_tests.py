import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasicInstallTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Сайт Блог!', self.browser.title)
        # self.fail('Finish the test!')

    def test_home_page_header(self):
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Денис', header.text)

    def test_home_page_blog(self):
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(
            By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_element(
            By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_home_page_article_title_link_leads_to_article_page(self):
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(
            By.CLASS_NAME, 'article-title')

        article_link = self.browser.find_element(
            By.TAG_NAME, 'a')
        self.browser.get(article_link.get_attribute('href'))

        article_page_title = self.browser.find_element(
            By.CLASS_NAME, 'article-title')
        self.assertEqual(article_title.text, article_page_title.text)

    # Попытка открыть несуществующую статью, открылась красивая страничка "Страница не найдена"


if __name__ == '__main__':
    unittest.main()
