def una_minuscola1(s):
    for c in s: #controlla solo il primo carattere
        if c.islower():
            return True
        else:
            return False

def una_minuscola2(s):
    for c in s: #controlla che 'c' sia minuscola (e la è sempre)
        if 'c'.islower():
            return 'True' #non sono booleani
        else:
            return 'False'

def una_minuscola3(s):
    for c in s: #controlla l'ultima perché flag viene sovrascritto ogni volta
        flag = c.islower()
    return flag

def una_minuscola4(s): #funziona correttamente
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def una_minuscola5(s): #non controlla se c'è almeno una lettera minuscola, ma solo se tutte le lettere sono minuscole
    for c in s:
        if not c.islower():
            return False
    return True

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 8.4
    text:
    Tutte le funzioni che seguono dovrebbero controllare se una stringa contiene almeno una lettera minuscola, ma qualcuna di esse è
    sbagliata. Per ogni funzione, descrivete cosa fa in realtà (supponendo che il parametro sia una stringa).

        def una_minuscola1(s):
            for c in s:
                if c.islower():
                    return True
                else:
                    return False

        def una_minuscola2(s):
            for c in s:
                if 'c'.islower():
                    return 'True'
                else:
                    return 'False'

        def una_minuscola3(s):
            for c in s:
                flag = c.islower()
            return flag

        def una_minuscola4(s):
            flag = False
            for c in s:
                flag = flag or c.islower()
            return flag

        def una_minuscola5(s):
            for c in s:
                if not c.islower():
                    return False
            return True
    """
    s = "cIAO"
    print(una_minuscola1(s))
    print(una_minuscola2(s))
    print(una_minuscola3(s))
    print(una_minuscola4(s))
if __name__ == '__main__':
    main()