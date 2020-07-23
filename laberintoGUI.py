import turtle

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Laberinto_Prolog_Python')

wn.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(3)

nivel = []

def abre_archivo(archivo_txt):
    #return [[elemento for elemento in x if(elemento!='\n' and elemento!=' ')]for x in open(archivo_txt,"r").readlines() ]
    return open(archivo_txt,"r").readlines()

# Definir primer nivel
nivel_prueba = (lambda x: abre_archivo(x))("laberinto.txt")

# nivel_1 = [
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXX     XXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXX        XXXXX",
#     "XXXXXXXXXXXX        XXXXX",
#     "XXXX     XXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
#     "XXXXXXXXXXXXXXXXXXXXXXXXX",
# ]

nivel.append(nivel_prueba)

def start(nivel):
    for file in range(len(nivel)):
        for column in range(len(nivel[file])):
            letra_x = nivel[file][column]
            screen_x = -288 + (column * 24)
            screen_y = 288 - (file * 24)

            if letra_x == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

pen = Pen()
start(nivel[0])
turtle.done()

conecta(i, 2).
conecta(1, 7).
conecta(2, 3).
conecta(2, 8).
conecta(3, 4).
conecta(3, 9).
conecta(4, 10).
conecta(5, 6).
conecta(5, 11).
conecta(7, 13).
conecta(8, 9).
conecta(10, 16).
conecta(11, 17).
conecta(12, 18).
conecta(13, 14).
conecta(14, 15).
conecta(14, f).
conecta(16, 22).
conecta(22, 21).
conecta(21, 15).