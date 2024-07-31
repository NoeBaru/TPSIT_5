import math

def mia_radq(a, epsilon):
    x = a
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:  
            break
        x = y
    return x

def test_radq(a, epsilon):
    print(f"{'a':<6} {'mia_radq(a)':<14} {'math.sqrt(a)':<14} {'diff':<14}")
    print(f"{'-':<6} {'----------':<14} {'------------':<14} {'----':<14}")
    for valore in a:
        custom_sqrt = mia_radq(valore, epsilon)
        math_sqrt = math.sqrt(valore)
        diff = abs(custom_sqrt - math_sqrt)
        print(f"{valore:<6.1f} {custom_sqrt:<14.10f} {math_sqrt:<14.10f} {diff:<14.10f}")

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 7.1
    text:
    Copiate il ciclo del Paragrafo 7.5 e incapsulatelo in una funzione di nome mia_radq
    che prenda a come parametro, scelga un valore appropriato di x, e restituisca una stima del valore
    della radice quadrata di a.
    Quale verifica, scrivete una funzione di nome test_radq che stampi una tabella come questa:
        a mia_radq(a) math.sqrt(a) diff
        - ---------- ------------ ----
        1.0 1.0 1.0 0.0
        2.0 1.41421356237 1.41421356237 2.22044604925e-16
        3.0 1.73205080757 1.73205080757 0.0
        4.0 2.0 2.0 0.0
        5.0 2.2360679775 2.2360679775 0.0
        6.0 2.44948974278 2.44948974278 0.0
        7.0 2.64575131106 2.64575131106 0.0
        8.0 2.82842712475 2.82842712475 4.4408920985e-16
        9.0 3.0 3.0 0.0
    La prima colonna è un numero, a; la seconda è la radice quadrata di a calcolata con mia_radq; la
    terza è la radice quadrata calcolata con math.sqrt; la quarta è il valore assoluto della differenza tra
    le due stime.
    """
    epsilon = 1e-10
    a = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    test_radq(a, epsilon)
if __name__ == '__main__':
    main()