import socket
import threading
import sqlite3

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
DB_NAME = "file.db"

'''
QUERY consegne:
1. chiedere al server se un certo nome file è presente;
2. chiedere al server il numero di frammenti di un file a partire dal suo nome file;
3. chiedere al server l'IP dell'host che ospita un frammento a partire nome file e dal numero del frammento;
4. chiedere al server tutti gli IP degli host sui quali sono salvati i frammenti di un file a partire dal nome file.

QUERY schema:
    messaggio: nome azione/metodo|argomento
    1.
        client --> server: checkFile|fileName
        server --> client: checkFile|isFound (boolean)
    2.
        client --> server: numFrag|fileName
        server --> client: numFrag|numberF
    3.
        client --> server: searchHostIp|fileName|numFrag
        server --> client: searchHostIp|hostIp
    4.
        client --> server: searchAllIp|fileName
        server --> client: searchAllIp|hostIp1|hostIp2...
'''

class ClientHandler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        dbConn = sqlite3.connect(DB_NAME) #file del db
        cursor = dbConn.cursor() #per le query

        while True:
            message = self.connection.recv(BUFFER_SIZE).decode()
            print(message)
            campi = message.split("|")
            response = ""

            #query n1
            if campi[0] == "checkFile": #[checkFile, fileName]
                '''
                SELECT *
                FROM files
                WHERE nome = fileName
                '''
                isFound = False
                cursor.execute("SELECT * FROM files WHERE nome = ?", (campi[1],))#1 query (cerca se c'è un file nel db)
                result = cursor.fetchone()
                if result and result[0]: #prende il risultato della query (riga) e lo converte in un boolean
                    isFound = True
                    
                response = f"{campi[0]}|{isFound}" #se isFound è null non lo ha trovato
            
            #query n2
            elif campi[0] == "numFrag": #[numFrag, fileName]
                '''
                SELECT tot_frammenti
                FROM files
                WHERE nome = ?
                '''
                cursor.execute("SELECT tot_frammenti FROM files WHERE nome = ?", (campi[1],))#1 query (cerca se c'è un file nel db)
                result = cursor.fetchone()
                numberF = 0

                if result:
                    numberF = result[0] #se trovo un num di frag li restituisce
                
                response = f"{campi[0]}|{numberF}"

            #query n3
            elif campi[0] == "searchHostIp":
                '''
                SELECT host
                FROM frammenti
                INNER JOIN files ON files.id_file = frammenti.id_file
                WHERE files.nome = ?
                AND frammenti.n_frammento = ?
                '''
                cursor.execute("SELECT host FROM frammenti INNER JOIN files ON files.id_file = frammenti.id_file WHERE files.nome = ? AND frammenti.n_frammento = ?", (campi[1],campi[2]))
                
                result = cursor.fetchone()
                if result:
                    hostIp = result[0]
                else:
                    hostIp = "Not Found"
                response = f"{campi[0]}|{hostIp}"

            #query n4
            elif campi[0] == "searchAllIp": #[searchAllIp, fileName]
                '''
                SELECT host
                FROM frammenti
                INNER JOIN files ON files.id_file = frammenti.id_file
                WHERE files.nome = ?
                AND frammenti.n_frammento = ?
                '''
                cursor.execute("SELECT host FROM frammenti INNER JOIN files ON files.id_file = frammenti.id_file WHERE files.nome = ?", (campi[1],))
                # devo fare la fetchAll che deve scorrere gli host e salvarli in result (usando un for result in results)
                result = cursor.fetchall()
                if result:
                    hostIpList = []
                    for row in result:
                        hostIpList.append(row[0])
                        hostIp = "|".join(hostIpList)
                else:
                    hostIp = "Not Found"

                
                response = f"{campi[0]}|{hostIp}"

            #per uscire
            elif campi[0] == "exit":
                self.kill()
                break

            self.connection.sendall(response.encode()) #manda la risposta
    def kill(self):
        self.connection.close()

def main():
    """
    Author: Noemi Baruffolo
    date: 07/11/2024
    es. preparazione verifica (server tcp)
    text: vedi "Esercitazione - preparazione alla verifica" su Classroom
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, clientAddress = s.accept() #bloccante
        print(f"Il client {clientAddress} si è connesso")
        thread = ClientHandler(connection)
        thread.start()

if __name__ == '__main__':
    main()