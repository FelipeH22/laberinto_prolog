from pyswip import *
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

lista_archivo = abre_archivo("laberinto.txt")
parejas_fila = p_fila(lista_archivo,[]) # Obtener parejas que se encuentran en la misma fila
lista_limpia = list(map(quitar,lista_archivo)) #Se quitan "|" de las listas.
parejas_columna = p_col(lista_limpia,[])# Obtener parejas que se encuentran en la misma columna 
lista_hechos= parejas_fila+parejas_columna #Lista con parejas de filas y columnas

prolog = Prolog()

for i in list(map(hechos,lista_hechos)):# Se crean hechos de forma dinámica
    prolog.assertz(i)

#Reglas para obtener la solución del laberinto
prolog.assertz('conectado(Pos1,Pos2) :- conecta(Pos1,Pos2)')
prolog.assertz('conectado(Pos1,Pos2) :- conecta(Pos2,Pos1)')
prolog.assertz('miembro(X,[X|_])')
prolog.assertz('miembro(X,[_|Y]) :- miembro(X,Y)')
prolog.assertz('camino([f|RestoDelCamino],[f|RestoDelCamino])')
prolog.assertz('camino([PosActual|RestoDelCamino],Sol) :- conectado(PosActual,PosSiguiente),'
                '\+ miembro(PosSiguiente,RestoDelCamino),'
                'camino([PosSiguiente,PosActual|RestoDelCamino],Sol)')


soluciones_lab = []
x = []
for i in prolog.query('camino([i],Sol)'):#Obtener las soluciones al laberinto
    soluciones_lab.append(i)

for i in soluciones_lab:#Almacenar las soluciones en la lista x
    x.append(i['Sol'])
print(x)