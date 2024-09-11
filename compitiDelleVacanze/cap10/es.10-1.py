def somma_nidificata(lista_nidificata):
    somma_totale = 0
    for sottolista in lista_nidificata:
        somma_totale += sum(sottolista)
    return somma_totale

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.1
    text:
    Scrivete una funzione di nome somma_nidificata che prenda una lista di liste di numeri interi e sommi gli elementi di tutte le
    liste nidificate. Esempio:
        >>> t = [[1, 2], [3], [4, 5, 6]]
        >>> somma_nidificata(t)
        21
    Potete scaricare le soluzioni degli esercizi seguenti all'indirizzo http://thinkpython2.com/code/list_exercises.py.
    """
    t = [[1, 2], [3], [4, 5, 6]]
    risultato = somma_nidificata(t)
    print(f"La somma degli elementi della lista nidificata è: {risultato}")

if __name__ == '__main__':
    main()
