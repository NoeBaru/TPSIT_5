import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

def main():
    """
    Author: Noemi Baruffolo
    date: 07/11/2024
    es. preparazione verifica (client tcp)
    text: vedi "Esercitazione - preparazione alla verifica" su Classroom
    """

    # Dizionario delle query disponibili
    queries = {
        "1": "checkFile|dune.mov",
        "2": "numFrag|dune.mov",
        "3": "searchHostIp|dune.mov|8",
        "4": "searchAllIp|dune.mov"
    }

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)

    # Menu di selezione per l'utente
    while True:
        print("\nScegli una query da eseguire:")
        print("1. Verifica se un file è presente")
        print("2. Ottieni il numero di frammenti di un file")
        print("3. Ottieni l'IP dell'host di un frammento specifico")
        print("4. Ottieni tutti gli IP degli host che ospitano i frammenti di un file")
        print("5. Esci")

        choice = input("Inserisci il numero della query: ")

        if choice in queries:
            # Invia il messaggio associato alla query scelta
            messageClient = queries[choice]
            s.sendall(messageClient.encode())
            # Riceve e stampa la risposta del server
            messageServer = s.recv(BUFFER_SIZE)
            print(f"Ricevuto <{messageServer.decode()}> dal server")

        elif choice == "5":
            # Invia il messaggio di uscita
            messageExit = "exit"
            s.sendall(messageExit.encode())
            print("Disconnessione...")
            break

        else:
            print("Scelta non valida. Riprova.")

    s.close()

if __name__ == '__main__':
    main()