from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render,get_object_or_404 #for post_detail
from .forms import PostForm #for post_new
from django.shortcuts import redirect #for post_new


def post_list(request): #post_list view created
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blogApp/post_list.html',{'posts':posts})
#display post_list.html

def post_detail(request,pk):
    #pk is the primary key of the post and is passed on by the urls.py file to this view


    #post = Post.objects.get(pk=pk) can be used, but abad looking error is returned when the requested page is not found

    post = get_object_or_404(Post,pk=pk)
    return render(request,'blogApp/post_detail.html',{'post':post})



def post_new(request):
    if request.method == "POST":  #get or post method in form
        form = PostForm(request.POST)
        if(form.is_valid()):
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blogApp.views.post_detail',pk=post.pk) #display the newly inserted post
    else:   #display an empty form
        form=PostForm()
    return render(request,'blogApp/post_edit.html',{'form':form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blogApp.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogApp/post_edit.html', {'form': form})
