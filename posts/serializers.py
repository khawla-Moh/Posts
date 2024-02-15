from rest_framework import serializers
from .models import Posts,Comments,Category
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

from django.contrib.auth.models import User



class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:

        model=Comments
        fields=['user','text','created_at']


class PostListSerializer(serializers.ModelSerializer,TaggitSerializer,):

    category=serializers.StringRelatedField()
    tags = TagListSerializerField()
    class Meta:
        model=Posts
        fields=['author','name','content','publish_date','category','image','tags']
    
   


class PostDetailSerializer(serializers.ModelSerializer,TaggitSerializer):
    category=serializers.StringRelatedField()
    tags = TagListSerializerField()
    comment=PostCommentSerializer(source='comments_post',many=True)
   
    class Meta:
   
        model=Posts
        fields=['author','name','content','publish_date','category','image','tags','comment']
    

































































""" 
from django.contrib.auth.models import User

class UserSerilaizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']


class PostSerilaizers(serializers.ModelSerializer):
    author=UserSerilaizers()
    category=serializers.StringRelatedField()
    class Meta:
        model=Post              #form for model(Post)
        fields='__all__'         #all columns  appear in form 

from rest_framework import serializers
from .models import Comments
 """
