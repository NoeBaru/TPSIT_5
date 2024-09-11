def tronca(lista):
    if len(lista) > 2:
        del lista[0]
        del lista[-1]

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.4
    text:
    Scrivete una funzione di nome tronca che prenda una lista, la modifichi togliendo il primo e l'ultimo elemento, e restituisca None.
    Esempio:
        >>> t = [1, 2, 3, 4]
        >>> tronca(t)
        >>> t
        [2, 3]
    Potete scaricare le soluzioni degli esercizi seguenti all'indirizzo http://thinkpython2.com/code/list_exercises.py.
    """
    t = [1, 2, 3, 4]
    print(f"Lista originale: {t}")
    tronca(t)
    print(f"Lista dopo tronca(): {t}")

if __name__ == '__main__':
    main()
