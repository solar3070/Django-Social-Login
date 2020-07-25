from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogPost

def home(request):
    blog = Blog.objects
    return render(request, 'home.html', {'blog':blog})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'detail':details})

def create(request):
    if request.method == 'POST': 
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save() 
            return redirect('read')
    else:
        form = BlogPost()
        return render(request, 'write.html', {'form':form})

def update(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        form = BlogPost(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPost(instance = post)
        return render(request, 'write.html', {'form':form})

def delete(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    post.delete()
    return redirect('home')