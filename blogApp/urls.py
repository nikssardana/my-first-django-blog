from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    #post_list is a view (function) inside views.py that we will create
    #name=post_list is the name of url that we will use later on

    url(r'^post/(?P<pk>[0-9]+)/$',views.post_detail, name='post_detail'),
    
    url(r'^post/new/$',views.post_new,name='post_new'),

    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit,name='post_edit')

    ]
