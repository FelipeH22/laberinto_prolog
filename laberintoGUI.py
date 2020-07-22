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