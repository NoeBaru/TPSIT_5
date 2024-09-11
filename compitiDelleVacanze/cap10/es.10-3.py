def mediani(lista):
    return lista[1:-1] if len(lista) > 2 else []

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.3
    text:
    Scrivete una funzione di nome mediani che prenda una lista e restituisca una nuova lista che contenga tutti gli elementi, esclusi il
    primo e l'ultimo. Esempio:
        >>> t = [1, 2, 3, 4]
        >>> mediani(t)
        [2, 3]
    Potete scaricare le soluzioni degli esercizi seguenti all'indirizzo http://thinkpython2.com/code/list_exercises.py.
    """
    t = [1, 2, 3, 4]
    risultato = mediani(t)
    print(f"Gli elementi mediani della lista sono: {risultato}")

if __name__ == '__main__':
    main()
