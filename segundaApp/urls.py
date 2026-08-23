from django.contrib import admin
from django.urls import path
from segundaApp import views

urlpatterns = [
    path('segunda/', views.inicio),
    #Para se muestre en la primera pagina la ruta debe quedar vacia 
    # y tambien debe quedar vacia en el archivo de url principal
    path('saludo/', views.saludo)
]