import socket

def main():
    """
    Author: Noemi Baruffolo
    date: 12/09/2024
    Descrizione: Server echo che utilizza un socket UDP.
    """
    # Definisci l'IP e la porta del server
    server_ip = "127.0.0.1"  # Localhost
    server_port = 12345       # Porta arbitraria

    # Crea un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Associa l'indirizzo e la porta al socket
    sock.bind((server_ip, server_port))

    print(f"Server in ascolto su {server_ip}:{server_port}")

    while True:
        # Ricevi dati dal client
        data, addr = sock.recvfrom(1024)  # 1024 è la dimensione del buffer
        print(f"Messaggio ricevuto da {addr}: {data.decode()}")

        # Rispondi al client con lo stesso messaggio (echo)
        sock.sendto(data, addr)

if __name__ == '__main__':
    main()   
