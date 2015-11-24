from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post  #which model is to be used
        fields=('title','text') #which fields to show in form
