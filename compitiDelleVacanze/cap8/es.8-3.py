def palindromo(parola):
    return parola == parola[::-1]

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 8.3
    text: Nello slicing, si può specificare un terzo indice che stabilisce lo step o “passo”, cioè il numero di elementi da saltare
    tra un carattere estratto e il successivo. Uno step di 2 significa estrarre un carattere ogni 2 (uno sì, uno no), 3 significa
    uno ogni 3 (uno sì, due no), ecc.
        >>> frutto = 'banana'
        >>> frutto[0:5:2]
        'bnn'
    Uno step di -1 fa scorrere all'indietro nella parola, per cui lo slicing [::-1] genera una stringa scritta al contrario.
    Usate questo costrutto per scrivere una variante di una sola riga della funzione palindromo dell'Esercizio 6.3.
    def prima(parola):
        return parola[0]
    def ultima(parola):
        return parola[-1]
    def mezzo(parola):
        return parola[1:-1]
    """
    parole = ["palindromo", "banana", "anna", "civic", "radar"]
    for parola in parole:
        print(f"'{parola}' è un palindromo? {palindromo(parola)}")
if __name__ == '__main__':
    main()