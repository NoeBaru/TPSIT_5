def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 19.1
    text:
    La seguente funzione calcola ricorsivamente il coefficiente binomiale:
    def coeff_binomiale(n, k):
        #Calcola il coefficiente binomiale "n sopra k".
        #n: numero di prove
        #k: numero di successi
        #ritorna: int

        if k == 0:
        return 1
        if n == 0:
            return 0
        res = coeff_binomiale(n-1, k) + coeff_binomiale(n-1, k-1)
        return res
    Riscrivete il corpo della funzione usando delle espressioni condizionali nidificate.
    Nota: questa funzione non è molto efficiente, perché finisce per calcolare continuamente gli stessi valori. Potreste renderla più
    efficiente con la memoizzazione (vedere Paragrafo 11.6). Riscontrerete però che è difficile farlo, scrivendola con le espressioni 
    condizionali.
    """
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()