from django.shortcuts import render, HttpResponse

# Create your views here.
def profile(resquest):
    return HttpResponse('Página de Perfil')