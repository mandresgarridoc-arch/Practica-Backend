from django.shortcuts import render
import datetime
import random

# Create your views here.

def hora_actual(request):
    hora_ahora = datetime.datetime.now()
    contexto = {'hora': hora_ahora}
    return render(request, 'index.html', contexto)


"""def inicio_tercera(request):
    # Aqui solo llamo al archivo con render
    return render(request, 'index.html')"""

def dado(request):
    numero = random.randint(1,6)
    return render(request, 'dado.html', {'numero': numero})