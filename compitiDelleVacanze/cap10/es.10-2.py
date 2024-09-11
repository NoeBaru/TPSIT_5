def somma_cumulata(lista):
    somma = 0
    risultato = []
    for numero in lista:
        somma += numero
        risultato.append(somma)
    return risultato

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.2
    text:
    Scrivete una funzione di nome somma_cumulata che prenda una lista di numeri e restituisca la somma cumulata, cioè una nuova lista
    dove l'i-esimo elemento è la somma dei primi i + 1 elementi della lista di origine. Per esempio:
        >>> t = [1, 2, 3]
        >>> somma_cumulata(t)
        [1, 3, 6]
    Potete scaricare le soluzioni degli esercizi seguenti all'indirizzo http://thinkpython2.com/code/list_exercises.py.
    """
    t = [1, 2, 3]
    risultato = somma_cumulata(t)
    print(f"La somma cumulata è: {risultato}")

if __name__ == '__main__':
    main()
