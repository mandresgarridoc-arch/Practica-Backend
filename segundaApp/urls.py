from django.contrib import admin
from django.urls import path
from segundaApp import views

urlpatterns = [
    path('segunda/', views.inicio),
    path('', views.saludo)
]