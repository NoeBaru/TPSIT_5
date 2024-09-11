import random

class Carta:
    semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
    valori = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore

    def __str__(self):
        return f'{self.valore} di {self.seme}'

class Mazzo:
    def __init__(self):
        self.carte = [Carta(seme, valore) for seme in Carta.semi for valore in range(1, 14)]
        random.shuffle(self.carte)

    def pesca(self):
        return self.carte.pop() if self.carte else None

    def dai_mani(self, num_mani, carte_per_mano):
        mani = [Mano() for _ in range(num_mani)]
        for _ in range(carte_per_mano):
            for mano in mani:
                if self.carte:  #si assicura che ci siano carte nel mazzo
                    mano.aggiungi_carta(self.pesca())
        return mani

class Mano:
    def __init__(self):
        self.carte = []

    def aggiungi_carta(self, carta):
        self.carte.append(carta)

    def __str__(self):
        return ', '.join(str(carta) for carta in self.carte)

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 18.2
    text:
    Scrivete un metodo per Mazzo di nome dai_mani che prenda come parametri il numero di mani e il numero di carte da dare a ciascuna
    mano, e crei il numero stabilito di oggetti Mano, distribuisca il numero prefissato di carte a ogni mano e restituisca una lista
    delle Mani.
    """
    mazzo = Mazzo()
    mani = mazzo.dai_mani(4, 5)  #distribuisce 5 carte a ciascuna delle 4 mani
    for i, mano in enumerate(mani, 1):
        print(f'Mano {i}: {mano}')

if __name__ == '__main__':
    main()
