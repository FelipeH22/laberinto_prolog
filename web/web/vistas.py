from django.http import HttpResponse
from django.template import Template,Context

def muestra_laberinto(request):
    archivo = open("C:/Users/jfher/Desktop/2020-1/Modelos 2/laberinto_prolog/web/templates/laberinto.html")
    plt = Template(archivo.read())
    archivo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)