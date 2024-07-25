def main():
    """
    Author: Noemi Baruffolo
    date: //2024
    es. 18.1
    text: 
    Dato il seguente programma, disegnate un diagramma di classe UML (Unified Modeling Language) che illustri queste classi e le
    relazioni che intercorrono tra esse.
    class PingPongMadre:
        pass
    class Ping(PingPongMadre):
        def __init__(self, pong):
            self.pong = pong
    class Pong(PingPongMadre):
        def __init__(self, pings=None):
            if pings is None:
                self.pings = []
            else:
                self.pings = pings
        def add_ping(self, ping):
            self.pings.append(ping)
    pong = Pong()
    ping = Ping(pong)
    pong.add_ping(ping)
    """
    pass #non fa niente, così non da errori nel codice
if __name__ == '__main__':
    main()