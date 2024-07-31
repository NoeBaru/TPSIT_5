import math

def stima_pi():
    fattore = (2 * math.sqrt(2)) / 9801
    k = 0
    sommatoria = 0

    while True:
        numeratore = math.factorial(4 * k) * (1103 + 26390 * k)
        denominatore = (math.factorial(k) ** 4) * (396 ** (4 * k))
        termine = fattore * (numeratore / denominatore)
        sommatoria += termine
        
        if termine < 1e-15: #verifica se il termine è sufficientemente piccolo
            break
        k += 1
    
    piStimato = 1 / sommatoria
    return piStimato

def main():
    """
    Author: Noemi Baruffolo
    date: 2024
    es. 7.3
    text:
    Il matematico Srinivasa Ramanujan scoprì una serie infinita che può essere usata per generare un'approssimazione di 1/π:
        1/π = (2 * sqrt(2)) / 9801 * sum(k=0 to infinity) [ (4k)!(1103 + 26390k) / ((k!)^4 * 396^(4k)) ]
    Scrivete una funzione di nome stima_pi che utilizzi questa formula per calcolare e restituire una
    stima di π. Deve usare un ciclo while per calcolare gli elementi della sommatoria, fino a quando
    l'ultimo termine è più piccolo di 1e-15 (che è la notazione di Python per 10^-15). Controllate il
    risultato confrontandolo con math.pi.
    Soluzione: http://thinkpython2.com/code/pi.py
    """
    piStimato = stima_pi()
    print(f"Stima di π: {piStimato}")
    print(f"Valore di math.pi: {math.pi}")
    print(f"Differenza: {abs(piStimato - math.pi)}")

if __name__ == '__main__':
    main()
