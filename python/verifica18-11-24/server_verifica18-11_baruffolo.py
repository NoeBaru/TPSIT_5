import socket
import threading
import sqlite3
import time

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
DB_NAME = "fiumi.db"

'''
    messaggi schema:
    client--> server: "livello|dataOra|id_stazione"
    server-->client: "nome|localita|dataOra"
    3 query:
    1.server-->client: "checkMinLevel|livello"
      client-->server: "isMin|livello"
    2.server-->client: "checkMedLevel|livello"
      client-->server: "isMed|livello"
    3.server-->client: "checkMaxLevel|livello"
      client-->server:

    1.
    SELECT *
    FROM livelli
    WHERE livello < ? /100*30

    2.
    SELECT *
    FROM livelli
    WHERE livello >= ? /100*30
    AND livello < ? /100*70

    3.
    SELECT *
    FROM livelli
    WHERE livello >= ? /100*70
'''

def sirenaOn():
    print("Attivazione della sirena luminosa in corso...")

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

            if campi[0] == "checkMinLevel": #[checkMinimumLevel, level]                
                isMin = False
                cursor.execute('''
                SELECT *
                FROM livelli
                WHERE livello < ? /100*30
                '''
                , (campi[1],))#1 query 
                result = cursor.fetchone()
                if result and result[0]: #prende il risultato della query (riga) e lo converte in un boolean
                    isMin = True
                    
                response = f"{campi[0]}|{isMin}"

            elif campi[0] == "checkMedLevel": #[checkMedLevel, level]                
                isMed = False
                cursor.execute('''
                SELECT *
                FROM livelli
                WHERE livello >= ? /100*30
                AND livello < ? /100*70
                '''
                , (campi[1],))#2 query
                result = cursor.fetchone()
                if result and result[0]: #prende il risultato della query (riga) e lo converte in un boolean
                    isMed = True
                    print("ATTENZIONE: pericolo imminente! Il livello è fuori dal 30% al 70% di guardia")
                    
                response = f"{campi[0]}|{isMed}"

            elif campi[0] == "checkMaxLevel": #[checkMaxLevel, level]                
                isMax = False
                cursor.execute('''
                SELECT *
                FROM livelli
                WHERE livello >= ? /100*30
                AND livello < ? /100*70
                '''
                , (campi[1],))#3 query 
                result = cursor.fetchone()
                if result and result[0]: #prende il risultato della query (riga) e lo converte in un boolean
                    isMAx = True
                    sirenaOn()
                    print("ATTENZIONE: pericolo! Il livello supera il 70% di guardia")
                    
                response = f"{campi[0]}|{isMax}"

            print(f"Nome fiume: {""} località: {""} data e ora: {campi[2]}")

    def kill(self):
        self.connection.close()

def main():
    """
    Author: Noemi Baruffolo
    date: 18/11/2024
    es. verifica (server tcp)
    text: vedi testo su Classroom
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, clientAddress = s.accept() #bloccante
        print(f"Il client {clientAddress} si è connesso")
        thread = ClientHandler(connection)
        thread.start()
        time.sleep(15) #attende 15 sec prima di mandare un nuovo thread

if __name__ == '__main__':
    main()