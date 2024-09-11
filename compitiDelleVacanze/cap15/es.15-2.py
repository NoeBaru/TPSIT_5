import turtle
import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rettangolo:
    def __init__(self, larghezza, altezza, angolo_inferiore_sx):
        self.larghezza = larghezza
        self.altezza = altezza
        self.angolo_inferiore_sx = angolo_inferiore_sx  

class Cerchio:
    def __init__(self, centro, raggio):
        self.centro = centro 
        self.raggio = raggio

def disegna_rett(t, rettangolo):
    t.penup()
    t.goto(rettangolo.angolo_inferiore_sx.x, rettangolo.angolo_inferiore_sx.y)
    t.pendown()
    
    for _ in range(2):
        t.forward(rettangolo.larghezza)
        t.left(90)
        t.forward(rettangolo.altezza)
        t.left(90)

def disegna_cerchio(t, cerchio):
    t.penup()
    t.goto(cerchio.centro.x, cerchio.centro.y - cerchio.raggio)  #posiziona la tartaruga in basso rispetto al centro
    t.pendown()
    t.circle(cerchio.raggio)

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 15.2
    """
    window = turtle.Screen()
    
    t = turtle.Turtle()
    
    rettangolo = Rettangolo(200, 100, Punto(-100, -50))
    disegna_rett(t, rettangolo)

    cerchio = Cerchio(Punto(100, 100), 75)
    disegna_cerchio(t, cerchio)

    window.exitonclick()

if __name__ == '__main__':
    main()
