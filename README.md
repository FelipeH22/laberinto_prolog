# Laberinto desarrollado en Python y Prolog con interfaz web
### _Laberinto desarrollado con Prolog y Python en entorno web usando DJango_
##### Modelos de programación II - G.020-82

Laberinto estableciendo una comunicación entre Python y Prolog


#### Diagrama:


#### Descripción
_Laberinto resuelto mediante prolog y python_


#### Ejecutar proyecto
Creando un entorno virtual dentro del proyecto.
```
~$ pip install virtualenv
~$ virtualenv envProlog
```
Windows
```
~$ source envProlog/Script/active
~$ cd web
```
Linux
```
~$ source envProlog/bin/active
~$ cd web
```
Instalar librerías
```
~$ pip install -r requirements.txt
```
Ejecutar proyecto
```
~$ python manage.py runserver
```

#### Ejecutar por consola
```
~$ cd web/web
~$ python laberinto.py

```

#### Estructura del proyecto
+ web/
    + web/
    + static/
    + templates/
    + manage.py
    + generador_django.py
+ README.md
+ requirements.txt


#### SECRET_KEY
En caso de tener problemas con el SECRET_KEY, para ejecutar el proyecto en Django
ejecutar el siguiente archivo dentro del web/
```
~$ python laberinto.py

```
copiar el código en el archivo settings.py en del proyecto principal de Django.


#### Equipo de trabajo

Integrante  | Código
------------- | -------------
Cristhian Mauricio Yara Pardo | 20181020081
Juan Esteban Olaya García | 20171020135
Juan Felipe Herrera Poveda | 20181020077
