def ackermann(m, n, memo=None):
    if memo is None:
        memo = {}

    if (m, n) in memo:
        return memo[(m, n)]
    
    if m == 0:
        result = n + 1
    elif m > 0 and n == 0:
        result = ackermann(m - 1, 1, memo)
    elif m > 0 and n > 0:
        result = ackermann(m - 1, ackermann(m, n - 1, memo), memo)
    else:
        raise ValueError("I parametri m e n devono essere non negativi.")
    
    memo[(m, n)] = result
    return result

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 11.3
    text:
    Applicate la memoizzazione alla funzione di Ackermann dell'Esercizio 6.2 e provate a vedere se questa tecnica rende possibile il
    calcolo della funzione con argomenti più grandi. Suggerimento: no. Soluzione: http://thinkpython2.com/code/ackermann_memo.py
    """
    # Esempio di calcolo della funzione di Ackermann
    m, n = 3, 4
    print(f"Ackermann({m}, {n}) = {ackermann(m, n)}")

if __name__ == '__main__':
    main()
