from django.shortcuts import render, HttpResponse

#Modelos 
from .models import Proyect
# Create your views here.
def profile(resquest):
    projects = Proyect.objects.all()
    print(projects)
    return HttpResponse(projects)