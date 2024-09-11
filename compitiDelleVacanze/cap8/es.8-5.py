def ruota_parola(s, n):
    parolaRuotata = ""
    for char in s:
        if char.isalpha():  #controlla se il carattere è una lettera
            base = ord('A') if char.isupper() else ord('a')
            carattereRuotato = chr(((ord(char) - base + n) % 26) + base)
            parolaRuotata += carattereRuotato
        else:
            parolaRuotata += char  #aggiunge il carattere senza modifiche se non è una lettera
    return parolaRuotata

def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 8.5
    text:
    Un cifrario di Cesare è un metodo di criptazione debole che consiste nel “ruotare” ogni lettera di una parola di un dato numero di
    posti seguendo la sequenza alfabetica, ricominciando da capo quando necessario. Ad esempio 'A' ruotata di 3 posti diventa 'D',
    'Z' ruotata di 1 posto diventa 'A'.
    Per ruotare una parola, si ruota ciascuna delle sue lettere dello stesso numero di posti prefissato.
    Per esempio, “cheer” ruotata di 7 dà “jolly” e “melon” ruotata di -10 dà “cubed”. Nel film 2001:
    Odissea nello Spazio, il computer di bordo si chiama HAL, che non è altro che IBM ruotato di -1.
    Scrivete una funzione di nome ruota_parola che richieda una stringa e un intero come parametri, e che restituisca una nuova stringa
    che contiene le lettere della stringa di partenza ruotate della quantità indicata.
    Potete usare le funzioni predefinite ord, che converte un carattere in un codice numerico, e chr, che converte i codici numerici in
    caratteri. Le lettere sono codificate con il loro numero di ordine alfabetico, per esempio:
        >>> ord('c') - ord('a')
        2
    Dato che 'c' è la “2-esima” lettera dell'alfabeto. Ma attenzione: i codici numerici delle lettere maiuscole sono diversi.
    Su Internet, talvolta, vengono codificate in ROT13 (un cifrario di Cesare con rotazione 13) delle barzellette potenzialmente
    offensive. Se non siete suscettibili, cercatene qualcuna e decodificatela.
    Soluzione: http://thinkpython2.com/code/rotate.py .
    """
    s, n = input("Inserisci una parola e un numero intero separati da uno spazio: ").split()
    n = int(n)  #converti il secondo elemento in un numero intero
    parola_ruotata = ruota_parola(s, n)
    print(f"Parola originale: {s}, Parola ruotata: {parola_ruotata}")

if __name__ == '__main__':
    main()
