from collections import Counter

def piu_frequente(stringa):
    frequenze = Counter(stringa)
    
    lettere_ordinate = sorted(frequenze.items(), key=lambda x: x[1], reverse=True)
    
    for lettera, frequenza in lettere_ordinate:
        print(f"{lettera}: {frequenza}")

def main():
    """
    Author: Noemi Baruffolo
    date: 2024-09-11
    es. 12.2
    text:
    Scrivete una funzione di nome piu_frequente che riceva una stringa e stampi le lettere in ordine di frequenza decrescente.
    Trovate delle frasi di esempio in diverse lingue e osservate come varia la frequenza delle lettere. Confrontate i vostri risultati
    con le tabelle del sito http://en.wikipedia.org/wiki/Letter_frequencies.
    """

    stringa_inglese = "hello world"
    stringa_italiana = "ciao mondo"
    
    print("Frequenze lettere nella stringa inglese:")
    piu_frequente(stringa_inglese)
    
    print("\nFrequenze lettere nella stringa italiana:")
    piu_frequente(stringa_italiana)

if __name__ == '__main__':
    main()
