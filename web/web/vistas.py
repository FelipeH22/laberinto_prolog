from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render
from web import laberinto

def muestra_laberinto(request):
    laberinto = [
        [1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28,29,30],
        [31,32,33,34,35,36],
    ]
    return render(request, 'laberinto.html', {'laberinto':laberinto})

def resuelve_laberinto(request):
    laberint = [
        [1,2,3,4,5,6],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28,29,30],
        [31,32,33,34,35,36],
    ]
    cadena = laberinto.lista_def
    archivo = []
    for linea in cadena:
        archivo.append(str(linea))
    archivo.remove('f')
    archivo.remove('i')
    archivo=list(map(int, archivo))
    return render(request, 'solucion.html', {'archivo':archivo,'laberinto':laberint})
