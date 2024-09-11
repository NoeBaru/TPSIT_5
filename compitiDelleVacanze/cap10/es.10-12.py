def incastrabili(p1, p2):
    max_len = max(len(p1), len(p2))
    p1 = p1.ljust(max_len, '')
    p2 = p2.ljust(max_len, '')
    
    incastrata = ''.join(p1[i] + p2[i] for i in range(max_len))
    
    return incastrata

def trova_tris_parole(parole):
    tris = []
    n = len(parole)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p1, p2, p3 = parole[i], parole[j], parole[k]
                inter1 = incastrabili(p1, p2)
                if inter1 and inter1.startswith(p1) and inter1.endswith(p2):
                    inter2 = incastrabili(p1, p3)
                    if inter2 and inter2.startswith(p1) and inter2.endswith(p3):
                        inter3 = incastrabili(p2, p3)
                        if inter3 and inter3.startswith(p2) and inter3.endswith(p3):
                            tris.append((p1, p2, p3))
    
    return tris

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 10.12
    text:
    Due parole si “incastrano” se, prendendo le loro lettere alternativamente dall'una e dall'altra, si forma una nuova parola.
    1. Scrivete un programma che trovi tutte le coppie di parole che possono incastrarsi.
    2. Riuscite a trovare dei gruppi di tre parole che possono incastrarsi tra loro?
    """
    parole = ['shoe', 'cold', 'ace', 'bus', 'as']  # Esempio di parole
    
    #trova tutte le coppie di parole che possono incastrarsi
    print("Coppie di parole che possono incastrarsi:")
    for i in range(len(parole)):
        for j in range(i + 1, len(parole)):
            incastro = incastrabili(parole[i], parole[j])
            if incastro:
                print(f"{parole[i]} <-> {parole[j]} = {incastro}")

    #trova tutti i gruppi di tre parole che possono incastrarsi tra loro
    tris = trova_tris_parole(parole)
    print("\nGruppi di tre parole che possono incastrarsi tra loro:")
    for trio in tris:
        print(f"{trio[0]} <-> {trio[1]} <-> {trio[2]}")

if __name__ == '__main__':
    main()
