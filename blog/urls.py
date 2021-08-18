#Django 
from django.urls import path

#Mis Vistas 
from . import views

# Configuración de URL 
urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:id>/', views.post, name='post'),
]