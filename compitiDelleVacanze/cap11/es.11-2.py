def inverti_diz(dizionario):
    """
    Inverte il dizionario dato, con i valori originali come chiavi e le chiavi originali
    come valori in una lista associata a ciascuna chiave.
    
    :param dizionario: Dizionario da invertire.
    :return: Dizionario invertito.
    """
    inverted_dict = {}
    
    for key, value in dizionario.items():
        # Usa setdefault per ottenere una lista di valori associati alla chiave
        inverted_dict.setdefault(value, []).append(key)
    
    return inverted_dict

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 11.2
    text:
    Leggete la documentazione del metodo dei dizionari setdefault e usatelo per scrivere una versione più concisa di inverti_diz.
    """
    #esempio di dizionario da invertire
    dizionario = {'a': 1, 'b': 2, 'c': 1}
    print("Dizionario originale:", dizionario)
    
    inverted = inverti_diz(dizionario)
    print("Dizionario invertito:", inverted)

if __name__ == '__main__':
    main()
