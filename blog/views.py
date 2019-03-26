from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import Blogform


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

@login_required(login_url='/accounts/')
def create_blog(request):
    if request.method == 'POST':
        form = Blogform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_list')
    else:
        form = Blogform()
        return render(request,'blog/new_blog.html',{'form':form })
