from django.test import TestCase
from .models import Blog

# Create your tests here.

class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(title="how to enjoy life" , body="this is a very good subject")
        Blog.objects.create(title="how to lose you will to live" , body="this is a very bad subject")
    
    def test_title_of_blog(self):
        blog_one = Blog.objects.get(body = "this is a very good subject")
        self.assertEqual(blog_one.title , "how to enjoy life")
        
        blog_two = Blog.objects.get(body = "this is a very bad subject")
        self.assertEqual(blog_two.title , "how to lose you will to live")
        
    
    def test_body_of_blog(self):
        blog_one = Blog.objects.get(title = "how to enjoy life")
        self.assertEqual(blog_one.body , "this is a very good subject")
        
        blog_two = Blog.objects.get(title = "how to lose you will to live")
        self.assertEqual(blog_two.body , "this is a very bad subject")