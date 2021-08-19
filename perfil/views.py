from django.shortcuts import render

#Modelos 
from .models import Proyect
# Create your views here.
def profile(resquest):
    projects = Proyect.objects.all()

    return render(resquest, 'profile.html', {'projects': projects})