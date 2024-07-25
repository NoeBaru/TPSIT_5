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
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()