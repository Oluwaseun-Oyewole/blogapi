from django.db.models import fields
from .models import *
from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created',)
    

class UserSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')