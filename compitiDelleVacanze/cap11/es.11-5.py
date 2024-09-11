def ruota_parola(parola1, parola2):
    if len(parola1) != len(parola2):
        return False
    return parola2 in (parola1 * 2)

def trova_coppie_ruotabili(lista_parole):
    coppie_ruotabili = []
    parole_set = set(lista_parole) 
    
    for parola1 in parole_set:
        for parola2 in parole_set:
            if parola1 != parola2 and ruota_parola(parola1, parola2):
                coppie_ruotabili.append((parola1, parola2))
    
    return coppie_ruotabili

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 11.5
    text:
    Due parole sono “ruotabili” se potete far ruotare le lettere dell'una per ottenere l'altra (vedere ruota_parola nell'Esercizio 8.5).
    Scrivete un programma che legga un elenco di parole e trovi tutte le coppie di parole ruotabili.
    """
    
    lista_parole = ["abc", "bca", "cab", "xyz", "zxy", "yzx"]
    
    coppie = trova_coppie_ruotabili(lista_parole)
    print("Coppie di parole ruotabili:", coppie)

if __name__ == '__main__':
    main()
