#Django
from django.shortcuts import render, HttpResponse

#Models 
from .models import Post
# Create your views here.
def posts(resques):
    posts = Post.objects.all()
    return HttpResponse(posts)

def post(request, id):
    post = Post.objects.get(id=id)
    return HttpResponse(post)
