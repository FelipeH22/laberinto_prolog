from pyswip import Prolog
prolog = Prolog()
prolog.consult('laberinto.pl')
list(prolog.query('sol'))
