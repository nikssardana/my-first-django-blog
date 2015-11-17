from django.shortcuts import render

def post_list(request): #post_list view created
    return render(request,'blogApp/post_list.html',{})
#display post_list.html
