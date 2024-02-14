from django.db import models
from taggit.managers import TaggableManager

from django.contrib.auth.models import User

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=16)
    def __str__(self) :
        return self.name


class Posts(models.Model):
    author=models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    content=models.TextField(max_length=300)
    publish_date=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,related_name='post_category',on_delete=models.SET_NULL,null=True)
    tags = TaggableManager() 
    image=models.ImageField(upload_to='post')
    

    def __str__(self) :
        return self.name 



class Comments(models.Model):
    post=models.ForeignKey(Posts,related_name='comments_post',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='comments_user',on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

    
    def __str__(self) :
        return self.user