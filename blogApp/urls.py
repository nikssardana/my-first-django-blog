from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    #post_list is a view (function) inside views.py that we will create
    #name=post_list is the name of url that we will use later on
    
    ]