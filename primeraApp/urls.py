from django.contrib import admin
from django.urls import path
from primeraApp import views

urlpatterns = [
    path('primera/', views.inicio),
    path('hora/', views.hora)
]