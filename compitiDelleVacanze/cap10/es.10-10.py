import bisect

def bisezione(lista, valore):
    inizio = 0
    fine = len(lista) - 1
    
    while inizio <= fine:
        metà = (inizio + fine) // 2
        if lista[metà] == valore:
            return True
        elif lista[metà] < valore:
            inizio = metà + 1
        else:
            fine = metà - 1
    
    return False

def bisezione_con_bisect(lista, valore):
    indice = bisect.bisect_left(lista, valore)
    return indice < len(lista) and lista[indice] == valore

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.10
    text:
    Scrivete una funzione di nome bisezione che richieda una lista ordinata e un valore da ricercare, e restituisca True se la parola fa parte della lista,
    o False se non è presente.
    """
    parole = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']
    parola_da_cercare = 'cherry'
    
    trovata = bisezione(parole, parola_da_cercare)
    print(f"Ricerca manuale: La parola '{parola_da_cercare}' è presente? {trovata}")
    
    trovata_bisect = bisezione_con_bisect(parole, parola_da_cercare)
    print(f"Ricerca con bisect: La parola '{parola_da_cercare}' è presente? {trovata_bisect}")

if __name__ == '__main__':
    main()
