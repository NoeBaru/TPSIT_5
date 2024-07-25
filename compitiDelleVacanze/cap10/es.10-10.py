def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.10
    text:
    Per controllare se una parola è contenuta in un elenco, è possibile usare l'operatore in, ma è un metodo lento, perché ricerca le
    parole seguendo il loro ordine. Dato che le parole sono in ordine alfabetico, possiamo accelerare l'operazione con una ricerca
    binaria (o per bisezione), che è un po' come cercare una parola nel vocabolario. Partite nel mezzo e controllate se la parola che
    cercate viene prima o dopo la parola di metà elenco. Se prima, cercherete nella prima metà nello stesso modo, se dopo, cercherete
    nella seconda metà. Ad ogni passaggio, dimezzate lo spazio di ricerca. Se l'elenco ha 113.809 parole, ci vorranno circa 17 passaggi
    per trovare la parola o concludere che non c'è. Scrivete una funzione di nome bisezione che richieda una lista ordinata e un valore
    da ricercare, e restituisca True se la parola fa parte della lista, o False se non è presente. Oppure, potete leggere la
    documentazione del modulo bisect e usare quello! Soluzione: http://thinkpython2.com/code/inlist.py
    """
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()