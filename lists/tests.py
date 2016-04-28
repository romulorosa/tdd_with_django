from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
import re
from lists.views import home_page

# Create your tests here.

class HomePageViewTest(TestCase):

    def test_home_page_uses_home_template(self):
        request = HttpRequest()
        response = home_page(request)
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        observed_content = re.sub(csrf_regex,'',response.content.decode('utf8'))
        expected_content = render_to_string('home.html')
        self.assertEqual(observed_content, expected_content)

    def test_home_page_can_store_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'new item'
        response = home_page(request)

        expected_content = render_to_string(
            'home.html',
            {'new_item_text': 'new_item'}
        )

        self.assertIn(
            '<td>new item</td>',
            response.content.decode('utf8')
        )
