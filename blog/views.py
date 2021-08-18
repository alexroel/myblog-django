from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def posts(resques):
    return HttpResponse('Págia de publicaciones')

def post(request, id):
    return HttpResponse('Mi Blog')
