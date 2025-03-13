from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .serializers import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404

class PostList(ListCreateAPIView):
    """Getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
        
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    """"getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
#the same method with viewset
class PostViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
    
    def list(self, request):
        Serializer = self.serializer_class(self.queryset,many=True)
        return Response (Serializer.data)
    
    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset,pk=pk)
        Serializer = self.serializer_class(post_object)
        return Response(Serializer.data)
        

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass