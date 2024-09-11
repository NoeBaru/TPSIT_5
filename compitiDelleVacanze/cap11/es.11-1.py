def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    text:
    Scrivete una funzione che legga le parole in words.txt e le inserisca come chiavi in un dizionario. I valori non hanno importanza.
    Usate poi l'operatore in come modo rapido per controllare se una stringa è contenuta nel dizionario. Se avete svolto l'Esercizio
    10.10, potete confrontare la velocità di questa implementazione con l'operatore in applicato alla lista e la ricerca binaria.
    """

    #legge le parole dal file e le inserisce nel dizionario
    word_dict = {}
    try:
        with open('words.txt', 'r') as file:
            for line in file:
                word = line.strip()
                word_dict[word] = None

    except FileNotFoundError:
        print("Il file 'words.txt' non è stato trovato.")
        return

    #verifica se una stringa è contenuta nel dizionario
    test_string = 'esempio'  #modifica questa stringa per testare altre parole

    if test_string in word_dict:
        print(f"La parola '{test_string}' è contenuta nel dizionario.")
    else:
        print(f"La parola '{test_string}' non è contenuta nel dizionario.")

if __name__ == '__main__':
    main()
