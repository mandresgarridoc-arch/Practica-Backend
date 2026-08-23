from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def inicio (request):
    return HttpResponse("<h1>Primera pagina con django</h1>")

def hora(request):
    hora_actual = datetime.datetime.now()
    salida = f"<h1>Hora actual: {hora_actual}</h1>"
    return HttpResponse(salida)
