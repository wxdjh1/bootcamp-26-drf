from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.models import Post
from main.serializers import PostSerializer


class PostViewsSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
