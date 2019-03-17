from django import forms
from .models import Blog


class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['user','blog_title','blog_subtitle','content']
