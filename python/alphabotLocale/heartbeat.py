recive_command, address1 = socket_command.accept()
recive_command, address2 = socket_command.accept()

thread.

def heartbeat_receive(receive_heartbeat):
    socket_heartbeat.settimeout(6.5)
    while True:
        try:
            data = receive_heartbeat.recv(4092)
            print("up")
        except socket.timeout:
            print("FERMA TUTTO")
            break
        except Exception as e:
            print(f"Si è verificato un errore: {e}")
            break

    socket_heardbeat.close()
    socket_command.close()
    # Alphabot.stop() 