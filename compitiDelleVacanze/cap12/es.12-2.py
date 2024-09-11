from collections import defaultdict

def leggi_parole(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def costruisci_dizionario_anagrammi(parole):
    dizionario_anagrammi = defaultdict(list)
    
    for parola in parole:
        chiave = ''.join(sorted(parola)) 
        dizionario_anagrammi[chiave].append(parola)
    
    return dizionario_anagrammi

def stampa_anagrammi(dizionario_anagrammi):
    gruppi_anagrammi = [sorted(gruppa) for gruppa in dizionario_anagrammi.values() if len(gruppa) > 1]
    
    gruppi_ordinati = sorted(gruppi_anagrammi, key=len, reverse=True)
    
    for gruppo in gruppi_ordinati:
        print(gruppo)

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 12.2
    text:
    Ancora anagrammi!
    1. Scrivete un programma che legga un elenco di parole da un file e stampi tutti gli insiemi di parole che sono
    tra loro anagrammabili. Un esempio di come si può presentare il risultato:
        ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
        ['retainers', 'ternaries']
        ['generating', 'greatening']
        ['resmelts', 'smelters', 'termless']
    Suggerimento: potete costruire un dizionario che faccia corrispondere un gruppo di lettere con una lista di parole che si possono
    scrivere con quelle lettere. Il problema è: come rappresentare il gruppo di lettere in modo che possano essere usate come chiave?
    2. Modificate il programma in modo che stampi la lista di anagrammi più lunga per prima, seguita dalla seconda più lunga, e così via.
    """
    file_path = 'parole.txt'
    parole = leggi_parole(file_path)
    dizionario_anagrammi = costruisci_dizionario_anagrammi(parole)
    stampa_anagrammi(dizionario_anagrammi)

if __name__ == '__main__':
    main()
