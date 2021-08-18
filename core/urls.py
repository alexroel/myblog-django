from django.urls import path
from . import views
# Configuración de URL 
urlpatterns = [
    path('', views.index, name='home'),
]