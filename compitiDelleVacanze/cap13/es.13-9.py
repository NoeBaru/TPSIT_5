def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 13.9
    text:
    Il “rango” di una parola è la sua posizione in un elenco di parole ordinate in base alla frequenza: la parola più comune ha rango 1,
    la seconda più comune rango 2, ecc. La legge di Zipf descrive una relazione tra rango e frequenza delle parole nei linguaggi naturali
    ( http://it.wikipedia.org/wiki/Legge_di_Zipf ), in particolare predice che la frequenza, f , della parola di rango r è:
        f = cr^-s
    dove s e c sono parametri che dipendono dal linguaggio e dal testo. Logaritmizzando ambo i lati dell'equazione, si ottiene:
        log f = log c - s log r
    che rappresentata su un grafico con log r in ascissa e log f in ordinata, è una retta di coefficiente angolare -s e termine noto
    log c. Scrivete un programma che legga un testo da un file, conti le frequenza delle parole e stampi una riga per ogni parola, in
    ordine decrescente di frequenza, con i valori di log f e log r. Usate un programma a vostra scelta per costruire il grafico dei
    risultati e controllare se formano una retta. Riuscite a stimare il valore di s? Soluzione: http://thinkpython2.com/code/zipf.py .
    Per avviare la mia risoluzione serve il modulo di plotting matplotlib. Se avete installato Anaconda, avete già matplotlib; altrimenti
    potrebbe essere necessario installarlo.
    """
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()