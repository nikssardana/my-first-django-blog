from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request): #post_list view created
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blogApp/post_list.html',{'posts':posts})
#display post_list.html
