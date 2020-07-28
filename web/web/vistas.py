from django.http import HttpResponse
from django.template import Template,Context
from web import laberinto

def muestra_laberinto(request):
    archivo = open("C:/Users/jfher/Desktop/2020-1/Modelos 2/laberinto_prolog/web/templates/laberinto.html")
    plt = Template(archivo.read())
    archivo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)
def resuelve_laberinto(request):
    cadena = laberinto.lista_def
    archivo = open("C:/Users/jfher/Desktop/2020-1/Modelos 2/laberinto_prolog/web/templates/solucion.html",'a+')
    for linea in cadena:
        archivo.write(str(linea))
    archivo.close()
    archivo = open("C:/Users/jfher/Desktop/2020-1/Modelos 2/laberinto_prolog/web/templates/solucion.html")
    plt = Template(archivo.read())
    archivo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)
