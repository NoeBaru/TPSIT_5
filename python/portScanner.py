import socket
import threading
import sqlite3
from ipaddress import ip_network #scorciatoia per cercare tutti gli ip di una determinata rete senza creare lunghe funzioni che lo facciano

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
DB_NAME = "ip_list.db"
network = "192.168.0.0/27" #rete network da cui partire
PORTS = [21, 22, 23, 25, 53, 80, 110, 123, 135, 139, 143, 443, 445, 993, 995, 3306, 3389] #porte più conosciute

#query: Interroga il database per estrarre l’elenco degli indirizzi IP con porte aperte, solo se è presente anche il nome dell’host.

#crea il database se non esiste già
def createDatabase():
    dbConn = sqlite3.connect(DB_NAME) #file del db
    cursor = dbConn.cursor() #per le query
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS "ipAddress" (
	"ip_host"	VARCHAR(15) NOT NULL,
	"nome_host"	VARCHAR(20),
	"port_list"	TEXT NOT NULL,
	PRIMARY KEY("ip_host")
    );
    ''')

#inserisce i dati nel database o li aggiunge a quelli già presenti se già ce ne sono all'interno
def insertDatabase(ip, name, port):
    dbConn = sqlite3.connect(DB_NAME) #file del db
    cursor = dbConn.cursor() #per le query
    cursor.execute(
    '''
    SELECT *
    FROM ipAddress
    WHERE ip_host = ?
    ''', (ip, )
    )
    result = cursor.fetchone()

    if result:
        cursor.execute(
        '''
        UPDATE ipAddress
        SET nome_host = ?, port_list = ?
        ''', (name, str(port))
    )
    else:
        cursor.execute(
        '''
        INSERT INTO "ipAddress"
        VALUES(?,?,?)
        ''', (ip, name, str(port)))
    dbConn.commit()
    dbConn.close()

#interroga il database per estrarre l’elenco degli indirizzi IP con porte aperte, ma solo se è presente anche il nome dell’host
def ipListPortOpenDatabase():
    dbConn = sqlite3.connect(DB_NAME) #file del db
    cursor = dbConn.cursor() #per le query
    cursor.execute(
    '''
    SELECT *
    FROM ipAddress
    WHERE nome_host IS NOT NULL
    ''')
    results = cursor.fetchall()
    for result in results:
        print(f"Risultato: {result}")
    dbConn.close()

class Scanner(threading.Thread):
    def __init__(self,ip):
        super().__init__()
        self.ip = str(ip)

    def run(self):
        dbConn = sqlite3.connect(DB_NAME) #file del db
        cursor = dbConn.cursor() #per le query
        hostName = ""
        openPorts = []
        
        #gestisco se prendere e stampare il nome host o restituire la sua assenza
        try:
            hostName = socket.gethostbyaddr(self.ip)[0] #prende il nome dell'host (se c'è)
            print(f"Nome host: {hostName}")
        except:
            print("Nessun nome host trovato!")
        
        #ciclo per cercare le porte aperte tra la lista delle più note che ho scelto
        for port in PORTS:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            isOpen = s.connect_ex((self.ip, port))

            if isOpen == 0: #se è aperta la aggiungo alla lista delle porte aperte
                openPorts.append(port)
        print(f"porte aperte: {openPorts}")

        insertDatabase(self.ip, hostName, openPorts) #inserisco i dati nel database        

def main():
    """
    Author: Noemi Baruffolo
    date: 16/11/2024
    es. port scanner
    text: vedi "Port scanner - Esercitazione" su Classroom
    """
    createDatabase() #creo il database se non esiste già
    threads = []

    #cerco tutti gli ip della rete assegnata e li scansiono
    for ip in ip_network(network, strict = False):
        #print(ip) #per testare
        thread = Scanner(ip)
        thread.start()
        threads.append(thread) #aggiungo il thread alla lista di threads
    
    for thread in threads:
        thread.join() #aspetta che tutti  thread abbiano finito

    ipListPortOpenDatabase()

if __name__ == '__main__':
    main()