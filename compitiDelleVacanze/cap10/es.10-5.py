def ordinata(lista):
    return lista == sorted(lista)

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.5
    text:
    Scrivete una funzione di nome ordinata che prenda una lista come parametro e restituisca True se la lista è ordinata in senso
    crescente, False altrimenti. Esempio:
        >>> ordinata([1, 2, 2])
        True
        >>> ordinata(['b', 'a'])
        False
    Potete scaricare le soluzioni degli esercizi seguenti all'indirizzo http://thinkpython2.com/code/list_exercises.py.
    """
    lista1 = [1, 2, 2]
    lista2 = ['b', 'a']
    print(f"La lista {lista1} è ordinata? {ordinata(lista1)}")
    print(f"La lista {lista2} è ordinata? {ordinata(lista2)}")

if __name__ == '__main__':
    main()
