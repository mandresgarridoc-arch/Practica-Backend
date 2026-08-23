from django.contrib import admin
from django.urls import path
from terceraApp import views

urlpatterns = [
    #Para se muestre en la primera pagina la ruta debe quedar vacia 
        # y tambien debe quedar vacia en el archivo de url principal
    path('', views.inicio_tercera),
    
]