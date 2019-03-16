from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.all().order_by('date')
    context = {
    'blogs':blogs,
    }
    return render(request,'blog/index.html', context)


def detail(request,pk):
    details = Blog.objects.get(pk=pk)
    context = {
    'details':details,
    }
    return render(request,'blog/details.html',context)
