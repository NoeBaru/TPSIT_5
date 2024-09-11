def trova_bifronti(lista):
    parole_set = set(lista)
    bifronti = []
    
    for parola in lista:
        parola_inversa = parola[::-1]
        if parola_inversa in parole_set and parola_inversa != parola:
            bifronti.append((parola, parola_inversa))
            parole_set.remove(parola)
    
    return bifronti
def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.11
    text:
    Una coppia di parole è “bifronte” se l'una si legge nel verso opposto dell'altra. Scrivete un programma che trovi tutte le parole
    bifronti nella lista di parole. Soluzione: http://thinkpython2.com/code/reverse_pair.py
    """
    parole = ['abba', 'baba', 'racecar', 'civic', 'deified', 'level', 'rotor', 'reviver', 'deified', 'baba']
    
    bifronti = trova_bifronti(parole)
    
    print("Parole bifronte trovate:")
    for coppia in bifronti:
        print(f"{coppia[0]} <-> {coppia[1]}")

if __name__ == '__main__':
    main()
