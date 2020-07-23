from pyswip import *
import re
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
def p_col(lis,lista):
    
    if lis == []:
        return None
    else:
        if len(lis) != 1:
            temp = lis[0]
            temp2 = lis[1]
            temp3 = lis[2]
            for i in range(0,len(temp)):
                if temp2[i] != "-" and len(lis)%2!=0:
                    lista += [[temp[i],temp3[i]]]
            p_col(lis[2:],lista)
        else: 
            p_col(lis[1:],lista)
    return lista

def abre_archivo(archivo_txt):
    lista_final = []
    lista = [x.split(' ') for x in open(archivo_txt,"r").readlines()]
    for i in lista:
        lista_final.append(i[:-1])
    return lista_final

def hechos(lista):
    return "conecta({},{})".format(str(lista[0]),str(lista[1]))

def quitar(lista):
    return list( filter(lambda x: x != "|", lista))

lis = abre_archivo("laberinto.txt")
#print(lis)
lista = p_fila(lis,[])
lista2 = list(map(quitar,lis))
#print(lista2)
lista_hechos = p_col(lista2,[])
lista_final= lista+lista_hechos
print(lista_final)
#print(list(map(hechos,lista_hechos)))

prolog = Prolog()
prolog.consult('laberinto.pl')
for i in list(map(hechos,lista_final)):
    print(i)
    prolog.assertz(i)

list(prolog.query('sol'))