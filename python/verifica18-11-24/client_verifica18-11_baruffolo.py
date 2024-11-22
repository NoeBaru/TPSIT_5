import socket
import datetime

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def menu():
    print('''
        1. livello < 30%
        2. 30% < livello < 70%
        3. livello >= 70%
        4.exit
          ''')

def main():
    """
    Author: Noemi Baruffolo
    date: 18/11/2024
    es. verifica (client tcp)
    text: vedi testo su Classroom
    """
    data = datetime.datetime.now()
    #dizionario delle query disponibili checkTypeLevel|livello|dataOra|id_stazione
    queries = {

        "1": f"checkMinLevel|1.22|{data}|3",
        "2": f"checkMedLevel|3.4|{data}|5",
        "3": f"checkMaxLevel|3.71|{data}|1",
    }

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)

    while True:
        #menu di selezione per l'utente
        menu() #stampa il menu' con le scelte disponibili delle query
        choice = input("Inserisci il numero della query: ")

        if choice in queries:
            #invia il messaggio associato alla query scelta
            messageClient = queries[choice]
            s.sendall(messageClient.encode())
            #riceve e stampa la risposta del server
            messageServer = s.recv(BUFFER_SIZE)
            print(f"Ricevuto <{messageServer.decode()}> dal server")

        elif choice == "4":
            #invia il messaggio di uscita
            messageExit = "exit"
            s.sendall(messageExit.encode())
            print("Disconnessione...")
            break

        else:
            print("Scelta non valida. Riprova.")

    s.close()

if __name__ == '__main__':
    main()