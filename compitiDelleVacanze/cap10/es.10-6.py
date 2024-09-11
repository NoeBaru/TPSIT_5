def anagramma(parola1, parola2):
    return sorted(parola1) == sorted(parola2)

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.6
    text:
    Due parole sono anagrammi se potete ottenerle riordinando le lettere di cui sono composte. Scrivete una funzione di nome anagramma
    che riceva due stringhe e restituisca True se sono anagrammi.
    Potete scaricare le soluzioni degli esercizi seguenti all'indirizzo http://thinkpython2.com/code/list_exercises.py.
    """
    parola1 = 'roma'
    parola2 = 'amor'
    print(f"Le parole '{parola1}' e '{parola2}' sono anagrammi? {anagramma(parola1, parola2)}")

    parola1 = 'ciao'
    parola2 = 'come'
    print(f"Le parole '{parola1}' e '{parola2}' sono anagrammi? {anagramma(parola1, parola2)}")

if __name__ == '__main__':
    main()
