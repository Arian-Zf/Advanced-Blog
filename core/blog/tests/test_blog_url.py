from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import PostList, PostListDetail



class TestUrl(SimpleTestCase):


    def test_blog_post_list_url_resolve(self):
        url = reverse('blog:post_list')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_blog_post_detail_url_resolve(self):
        url = reverse('blog:post_list_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, PostListDetail)