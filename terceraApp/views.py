from django.shortcuts import render
import datetime

# Create your views here.

def hora_actual(request):
    hora = datetime.datetime.now()
    return render(request, 'index.html', {'hora': hora})

def inicio_tercera(request):
    # Aqui solo llamo al archivo con render
    return render(request, 'index.html')