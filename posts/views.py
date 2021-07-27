from django.db.models import query
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from .permissions import isAuthorOrReadOnly


# Create your views here.


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    # def get_queryset(self):
    #     user = self.request.user
    #     return user.post_set.all()
    
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (isAuthorOrReadOnly,)
    