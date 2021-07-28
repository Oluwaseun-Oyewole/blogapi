from django.contrib.auth import get_user_model
from django.db.models import query
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer, UserSerializers
from rest_framework import generics, serializers, views
from .permissions import isAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import viewsets


# Create your views here.


class PostViews(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (isAuthorOrReadOnly,)


class UserViews(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    
    

# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
    
#     # def get_queryset(self):
#     #     user = self.request.user
#     #     return user.post_set.all()
    
    
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (isAuthorOrReadOnly,)
    
    
# class UserList(generics.ListAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializers
    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializers
    
