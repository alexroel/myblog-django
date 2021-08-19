#Django
from django.shortcuts import render

#Models 
from .models import Post
# Create your views here.
def posts(resques):
    posts = Post.objects.all()
    post = Post.objects.first()
    return render(resques, 'blogs.html', {'posts':posts, 'post':post })

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog.html', {'post':post})
