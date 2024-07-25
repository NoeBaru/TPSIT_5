def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 12.4
    text:
    Ed ecco un altro quesito di Car Talk: ( http://www.cartalk.com/content/puzzlers ): Qual è la più lunga parola inglese che rimane una
    parola valida se le togliete una lettera alla volta? Le lettere possono essere rimosse sia agli estremi o in mezzo, ma senza spostare
    le lettere rimanenti. Ogni volta che togliete una lettera, ottenete un'altra parola inglese. Se andate avanti, ottenete un'altra
    parola. Ora, voglio sapere qual è la parola più lunga possibile e quante lettere ha. Vi faccio un piccolo esempio: Sprite. Partite da
    sprite, togliete una lettera, una interna, come la r e resta la parola spite, poi togliete la e finale e avete spit, togliamo la s e
    resta pit, poi it, infine I. Scrivete un programma che trovi tutte le parole che sono riducibili in questa maniera, quindi trovate la
    più lunga. Questo esercizio è un po' più impegnativo degli altri, quindi eccovi alcuni suggerimenti:
    1. Potete scrivere una funzione che prenda una parola e calcoli una lista di tutte le parole che si possono formare togliendo una
    lettera. Queste sono le “figlie” della parola.
    2. Ricorsivamente, una parola è riducibile se qualcuna delle sue figlie è a sua volta riducibile. Come caso base, potete considerare
    riducibile la stringa vuota.
    3. L'elenco di parole che ho fornito, words.txt, non contiene parole di una lettera. Potete quindi aggiungere “I”, “a”, e la
    stringa vuota.
    4. Per migliorare le prestazioni del programma, potete memoizzare le parole che sono risultate riducibili.
    Soluzione: http://thinkpython2.com/code/reducible.py
    """
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()