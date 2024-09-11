def ha_duplicati(lista):
    return len(lista) != len(set(lista))

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.7
    text:
    Scrivete una funzione di nome ha_duplicati che richieda una lista e restituisca True se contiene elementi che compaiono più di una
    volta. Non deve modificare la lista di origine.
    Potete scaricare le soluzioni degli esercizi seguenti all'indirizzo http://thinkpython2.com/code/list_exercises.py.
    """
    lista1 = [1, 2, 3, 4]
    lista2 = [1, 2, 2, 4]
    print(f"La lista {lista1} ha duplicati? {ha_duplicati(lista1)}")
    print(f"La lista {lista2} ha duplicati? {ha_duplicati(lista2)}")

if __name__ == '__main__':
    main()
