from pyswip import Prolog
def p_fila(lis,lista):
    if lis == []:
        return lista
    temp=lis[0]
    for i in range(0,len(temp)-1):
        if(temp[i] != "|"):
            if(temp[i+1]!="|"):
                lista += [[temp[i],temp[i+1]]]
    p_fila(lis[1:],lista)

def abre_archivo(archivo_txt):
    return [[elemento for elemento in x if(elemento!='\n' and elemento!=' ')]for x in open(archivo_txt,"r").readlines() ]
    
lis = abre_archivo("laberinto.txt")
print(lis)
print(p_fila(lis,[]))
prolog = Prolog()
prolog.consult('laberinto.pl')
list(prolog.query('sol'))
