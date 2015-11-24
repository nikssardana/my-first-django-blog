from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render,get_object_or_404

def post_list(request): #post_list view created
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blogApp/post_list.html',{'posts':posts})
#display post_list.html

def post_detail(request,pk):
    #pk is the primary key of the post and is passed on by the urls.py file to this view


    #post = Post.objects.get(pk=pk) can be used, but abad looking error is returned when the requested page is not found

    post = get_object_or_404(Post,pk=pk)
    return render(request,'blogApp/post_detail.html',{'post':post})
