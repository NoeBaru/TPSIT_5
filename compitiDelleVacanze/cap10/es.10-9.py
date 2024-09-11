import time

def leggi_parole_append(filename):
    parole = []
    with open(filename, 'r') as f:
        for linea in f:
            parola = linea.strip()
            parole.append(parola)
    return parole

def leggi_parole_concatenazione(filename):
    parole = []
    with open(filename, 'r') as f:
        for linea in f:
            parola = linea.strip()
            parole = parole + [parola]
    return parole

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.9
    text:
    Scrivete una funzione che legga il file words.txt e crei una lista in cui ogni parola è un elemento. Scrivete due versioni della
    funzione, una che usi il metodo append e una il costrutto t = t + [x]. Quale richiede più tempo di esecuzione? Perché?
    Soluzione: http://thinkpython2.com/code/wordlist.py
    """
    filename = 'words.txt'

    start_time = time.time()
    parole_append = leggi_parole_append(filename)
    tempo_append = time.time() - start_time
    print(f"Tempo con append(): {tempo_append:.5f} secondi")

    start_time = time.time()
    parole_concatenazione = leggi_parole_concatenazione(filename)
    tempo_concatenazione = time.time() - start_time
    print(f"Tempo con concatenazione: {tempo_concatenazione:.5f} secondi")

if __name__ == '__main__':
    main()
