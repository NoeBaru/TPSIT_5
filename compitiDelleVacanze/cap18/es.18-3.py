def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 18.3
    text:
    Quelle che seguono sono le possibili combinazioni nel gioco del poker, in ordine crescente di valore e decrescente di probabilità:
    coppia: due carte dello stesso valore
    doppia coppia: due coppie di carte dello stesso valore
    tris: tre carte dello stesso valore
    scala: cinque carte con valori in sequenza (gli assi possono essere sia la carta di valore inferiore che quella di valore superiore,
           per cui Asso-2-3-4-5 è una scala, e anche 10-Fante-Regina-Re-Asso, ma non Regina-Re-Asso-2-3).
    colore: cinque carte dello stesso seme
    full: tre carte dello stesso valore più una coppia di carte dello stesso valore
    poker: quattro carte dello stesso valore
    scala reale: cinque carte dello stesso seme in scala (definita come sopra)
    Scopo di questo esercizio è stimare la probabilità di avere servita una di queste combinazioni.
    1. Scaricate i file seguenti da http://thinkpython2.com/codeCard.py :
    Versione completa delle classi Carta, Mazzo e Mano di questo capitolo.
    PokerHand.py : Implementazione incompleta di una classe che rappresenta una mano di poker con del codice di prova.
    2. Se eseguite PokerHand.py, serve delle mani di sette carte e controlla se qualcuna contenga un colore. Leggete attentamente il
       codice prima di proseguire.
    3. Aggiungete dei metodi a PokerHand.py di nome ha_coppia, ha_doppiacoppia, ecc. che restituiscano True o False a seconda che le mani
       soddisfino o meno il rispettivo criterio. Il codice deve funzionare indipendentemente dal numero di carte che contiene la mano
       (5 e 7 carte sono i casi più comuni).
    4. Scrivete un metodo di nome classifica che riconosca la combinazione più elevata in una mano e imposta di conseguenza l'attributo
       label. Per esempio, una mano di 7 carte può contenere un colore e una coppia; deve essere etichettata “colore”.
    5. Quando siete sicuri che i vostri metodi di classificazione funzionano, il passo successivo è stimare la probabilità delle varie
       mani. Scrivete una funzione in PokerHand.py che mescoli un mazzo di carte, lo divida in mani, le classifichi e conti quante volte
       compare ciascuna combinazione.
    6. Stampate una tabella delle combinazioni con le rispettive probabilità. Eseguite il vostro programma con numeri sempre più grandi
       di mani finché i valori ottenuti convergono ad un ragionevole grado di accuratezza. Confrontate i vostri risultati con i valori
       pubblicati su http://en.wikipedia.org/wiki/Hand_rankings .
    Soluzione: http://thinkpython2.com/code/PokerHandSoln.py .
    """
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()