from django.shortcuts import render,redirect
from .models import Posts,Category,Comments
from django.views.generic import ListView,DetailView
# Create your views here.


class PostList(ListView):
    model=Posts
    context_object_name = 'post'


class PostDetail(DetailView):
    model=Posts
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments']=Comments.objects.filter(post=self.get_object()).order_by('created_at')
        context['comments2']=Comments.objects.filter(post=self.get_object()).order_by('-created_at')
        return context

    






def add_commnet(request,slug):
    post=Posts.objects.get(slug=slug)
    comment=request.POST["comment"]
      
    Comments.objects.create(
        user=request.user,
        post=post,
        text=comment,
        )
    
    return redirect(f'/posts/{slug}')

 
