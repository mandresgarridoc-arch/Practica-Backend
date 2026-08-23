### Abrir primero CDM o Powershell

Primero revisar si python y Dajngo se encuentran instalados con los siguientes comandos:
- **python --version**
- **python -m django -version**

Luego actualizar pip con el comando:
- **python -m pip install --upgrade pip**

Si no estan instalados instar  Django con el comando
- **python pip install django**

Revisar los paquetes instalados:
- **pip list**

Para crear la aplicacion de Django:
- Primero buscar la ubicacion donde la crearemos por ejemplo el disco duro C:
- cd C:\Users\Ejemplo

En esta ubicacion creo el proyecto con el comando:
- **django-admin startproject ejemplo**\
El ejemplo se debe cambiar por el nombre del proyecto.\
Una vez creado, ingresar a la carpeta del proyecto con:
- **cd ejemplo**

Una vez dentro abrir la terminal de vscode con el comando:
- **code .** 

Desde la terminal de visual estudio abrir una nueva terminal para ejecutar el siguiente comando:
- **python manage.py runserver**

Dar ctrl + click en la direccion que muestra la terminal. 

--

Al crear las apps, primero se debe crear dos archivos llamados **urls.py** en cada app.

Etos archivos se deben poblar con lo siguiente:
-   from django.contrib import admin\
    from django.urls import path\
    from **nombre de la app** import views

urlpatterns = [\
    path('*direccion web*/', views.inicio),\
    path('*direccion web*/', views.hora)\
]

Esto se hace en **AMBOS** archivos urls.py.

Ir a el archivo urls.py **PRINCIPAL** y añadir el path de las urls en los archivos recien creados.

-   from *Nombre de la app* import views\
    from *Nombre de la segunda app* import views\

urlpatterns = [\
    path('*direccion de ejemplo/*', admin.site.urls),\
    path('*direccion de ejemplo 2/*', include('primeraApp.urls')),\
    #Esta ruta vacia es mi url principal, la primera que se muestra\
    path('', include('segundaApp.urls'))\
]

Para poner una de las rutas como principal, se deebn dejar dos comillas vacias en el archivo urls.py de la app y en el principal.




