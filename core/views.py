from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):

    class_name = 'class="home-body"'

    return render(request, 'home.html')

