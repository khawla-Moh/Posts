from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Posts,Category,Comments
from . import serializers



class PoststListAPI(generics.ListAPIView):
    queryset=Posts.objects.all()
    serializer_class=serializers.PostListSerializer
    


class PostDetailAPI(generics.RetrieveAPIView):
    queryset=Posts.objects.all()
    serializer_class=serializers.PostDetailSerializer    
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    ordering_fields = ['created_at']
            

class CommentListView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.PostCommentSerializer

    def get_queryset(self):
        order_by = self.request.query_params.get('order_by', 'new')
        if order_by == 'new':
            return Comments.objects.order_by('created_at')
        elif order_by == 'old':
            return Comments.objects.order_by('-created_at')
        else:
            return Comments.objects.all()       
    """ 
    def get(self, request, pk):
        post = Posts.objects.get(pk=pk)
        order_by = request.query_params.get('order_by', 'new')
        
        if order_by == 'old':
            comments = Comments.objects.filter(post=post).order_by('created_at')
        elif order_by == 'new':
            comments = Comments.objects.filter(post=post).order_by('-created_at')
        else:
            comments = Comments.objects.filter(post=post)
        
        comments_serializer =serializers.PostCommentSerializer(comments, many=True)
        return Response({'post': post, 'comments': comments_serializer.data})
    
    """

    
  



