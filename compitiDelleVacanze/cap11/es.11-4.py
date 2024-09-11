def ha_duplicati(lista):
    seen = {}  #dizionario per tenere traccia degli oggetti già visti
    
    for item in lista:
        if item in seen:
            return True
        seen[item] = True
    
    return False

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 11.4
    text:
    Se avete svolto l'Esercizio 10.7, avete già una funzione di nome ha_duplicati che richiede come parametro una lista e restituisce
    True se ci sono oggetti ripetuti all'interno della lista. Usate un dizionario per scrivere una versione più rapida e semplice di
    ha_duplicati. Soluzione: http://thinkpython2.com/code/has_duplicates.py
    """

    lista_con_duplicati = [1, 2, 3, 4, 2]
    lista_senza_duplicati = [1, 2, 3, 4, 5]
    
    print("Lista con duplicati:", ha_duplicati(lista_con_duplicati)) 
    print("Lista senza duplicati:", ha_duplicati(lista_senza_duplicati)) 

if __name__ == '__main__':
    main()
