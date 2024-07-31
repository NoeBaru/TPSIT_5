import math

def eval_ciclo():
    while True:
        dato = input('> ')
        if dato == 'fatto':
            break
        else:
            precDato = dato
        eval(dato)
        print(dato)
    print(dato)
    print(precDato)

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 7.2
    text:
    La funzione predefinita eval valuta un'espressione sotto forma di stringa, usando
    l'interprete Python. Ad esempio:
        >>> eval('1 + 2 * 3')
        7
        >>> import math
        >>> eval('math.sqrt(5)')
        2.2360679774997898
        >>> eval('type(math.pi)')
        <class 'float'>
    Scrivete una funzione di nome eval_ciclo che chieda iterativamente all'utente di inserire un dato,
    prenda il dato inserito e lo valuti con eval, infine visualizzi il risultato.
    Deve continuare fino a quando l'utente non scrive 'fatto', e poi restituire il valore dell'ultima
    espressione che ha valutato.
    """
    eval_ciclo()
if __name__ == '__main__':
    main()