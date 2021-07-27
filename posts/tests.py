from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class TestModelData(TestCase):
    
    @classmethod
    
    def setUpTestData(cls):
        
        # create user
        user1 = User.objects.create_user(username='seun', password='123')
        user1.save()
        
        # create post
        
        post1 = Post.objects.create(author=user1, title='blog post', body='This is my first blog post')
        post1.save()
        
        
    def test_blog_content(self):
        post1 = Post.objects.get(id=1)
        title = f'{post1.title}'
        author = f'{post1.author}'
        body = f'{post1.body}'
        
        # run test cases
        self.assertEqual(title, 'blog post')
        self.assertEqual(author, 'seun')
        self.assertEqual(body, 'This is my first blog post')