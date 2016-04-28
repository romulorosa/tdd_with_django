from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
# Create your tests here.

class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('<html><title>To-Do lists</title></html>', response.content.decode('utf-8'))
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertTrue(response.content.endswith(b'</html>'))
