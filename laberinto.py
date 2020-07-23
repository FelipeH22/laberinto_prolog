#from pyswip import Prolog

def p_fila(lis,lista):
    if lis == []:
        return None
    else:
        temp=lis[0]
        for i in range(0,len(temp)-1):
            if temp[i] != "|" and temp[i+1]!="|" and len(lis)%2!=0:
                lista += [[temp[i],temp[i+1]]]
        p_fila(lis[1:],lista)
    return lista

def abre_archivo(archivo_txt):
    lista = [x.split(' ') for x in open(archivo_txt,"r").readlines()]
    return lista

def hechos(lista):
    return "conecta({},{})".format(str(lista[0]),str(lista[1]))

lis = abre_archivo("laberinto.txt")
print(lis)
#lista_hechos = p_fila(lis,[])
#print(list(map(hechos,lista_hechos)))
#prolog = Prolog()
#prolog.consult('laberinto.pl')

#"""for i in list(map(hechos,lista_hechos)):
#    print(i)
#    prolog.assertz(i)
#print(list(prolog.query("conecta(i,2)")))"""
#print(list(prolog.query('sol')))
