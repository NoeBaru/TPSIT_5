import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Cerchio:    
    def __init__(self, centro, raggio):
        self.centro = centro
        self.raggio = raggio

class Rettangolo:    
    def __init__(self, larghezza, altezza, angolo_inferiore_sx):
        self.larghezza = larghezza
        self.altezza = altezza
        self.angolo_inferiore_sx = angolo_inferiore_sx  #punto in basso a sinistra

def distanza(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def punto_nel_cerchio(cerchio, punto):
    return distanza(cerchio.centro, punto) <= cerchio.raggio

def rett_nel_cerchio(cerchio, rettangolo):
    #verifica se tutti e quattro gli angoli del rettangolo sono nel cerchio
    angoli = [
        rettangolo.angolo_inferiore_sx,
        Punto(rettangolo.angolo_inferiore_sx.x + rettangolo.larghezza, rettangolo.angolo_inferiore_sx.y),
        Punto(rettangolo.angolo_inferiore_sx.x, rettangolo.angolo_inferiore_sx.y + rettangolo.altezza),
        Punto(rettangolo.angolo_inferiore_sx.x + rettangolo.larghezza, rettangolo.angolo_inferiore_sx.y + rettangolo.altezza)
    ]
    
    return all(punto_nel_cerchio(cerchio, angolo) for angolo in angoli)

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 15.1
    """
    #crea un cerchio con il centro nel punto (150, 100) e raggio 75
    centro = Punto(150, 100)
    cerchio = Cerchio(centro, 75)
    
    #crea un punto e verifica se è nel cerchio
    punto = Punto(150, 175)
    print(f"Il punto ({punto.x}, {punto.y}) è nel cerchio:", punto_nel_cerchio(cerchio, punto))
    
    #crea un rettangolo e verifica se è nel cerchio
    rettangolo = Rettangolo(50, 30, Punto(120, 90))
    print("Il rettangolo è interamente nel cerchio:", rett_nel_cerchio(cerchio, rettangolo))

if __name__ == '__main__':
    main()
