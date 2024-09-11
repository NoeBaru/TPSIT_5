from collections import defaultdict

def leggi_parole(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def trova_metatesi(parole):
    dizionario_per_lunghezza = defaultdict(list)
    
    for parola in parole:
        dizionario_per_lunghezza[len(parola)].append(parola)
    
    metatesi_coppie = []
    
    for lunghezza, lista_parole in dizionario_per_lunghezza.items():
        for i in range(len(lista_parole)):
            for j in range(i + 1, len(lista_parole)):
                parola1 = lista_parole[i]
                parola2 = lista_parole[j]
                if sono_metatesi(parola1, parola2):
                    metatesi_coppie.append((parola1, parola2))
    
    return metatesi_coppie

def sono_metatesi(parola1, parola2):
    if len(parola1) != len(parola2):
        return False
    
    differenze = []
    
    for i in range(len(parola1)):
        if parola1[i] != parola2[i]:
            differenze.append((parola1[i], parola2[i]))
            
            if len(differenze) > 2:
                return False
    
    return len(differenze) == 2 and differenze[0] == differenze[1][::-1]

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 12.3
    text:
    Si ha una metatesi quando una parola si può ottenere scambiando due lettere di un'altra parola, per esempio: “conversa” e “conserva”.
    Scrivete un programma che trovi tutte le coppie con metatesi nel dizionario. Suggerimento: non provate tutte le possibili coppie di
    parole e non provate tutti i possibili scambi. Soluzione: http://thinkpython2.com/code/metathesis.py.
    """
    file_path = 'parole.txt'
    parole = leggi_parole(file_path)
    coppie_metatesi = trova_metatesi(parole)
    
    for coppia in coppie_metatesi:
        print(coppia)

if __name__ == '__main__':
    main()
