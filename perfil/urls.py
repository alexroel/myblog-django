
#Django 
from django.urls import path

# mis Visatas 
from . import views

#Configuración de URLS
urlpatterns = [
    path('', views.profile, name='profile'),
]