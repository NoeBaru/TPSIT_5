def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 8.2
    text: Esiste un metodo delle stringhe di nome count che è simile alla funzione del Paragrafo 8.7.
    def contatoreLettera(parola):
        conta = 0
        for lettera in parola:
            if lettera == 'a':
                conta = conta + 1
        print(conta)
    parola = input("Inserisci una parola: ")
    contatoreLettera(parola)
    Leggete la documentazione del metodo e scrivete un'invocazione che conti il numero di a in 'banana'.
    """
    #parola = input("Inserisci una parola: ")
    parola = "banana"
    numeroA = parola.count('a')
    print(f"Il numero di 'a' in '{parola}' è: {numeroA}")
if __name__ == '__main__':
    main()