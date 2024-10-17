import socket
import threading

# import AlphaBot

# istanza = AlphaBot.alphabot()


def heartbeat_recive(recive_heartbeat):
    socket_heartbeat.settimeout(6.5)
    while True:
        try:
            data = recive_heartbeat.recv(4092)
            print("up")
        except socket.timeout:
            print("FERMA TUTTO")
            break  # Esci dal ciclo se c'è un timeout
        except Exception as e:
            print(f"Si è verificato un errore: {e}")
            break  # Esci dal ciclo in caso di errori non previsti

    socket_heartbeat.close()  # Chiudi il socket dopo l'uscita dal ciclo
    socket_command.close()
    # istanza.stop()


# Crea un socket TCP
socket_command = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_heartbeat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa il socket a un indirizzo e una porta
socket_command.bind(("localhost", 12345))
socket_heartbeat.bind(("localhost", 12346))

# il server ascolta le connessioni in entrata
socket_command.listen(1)  # Dimensione coda connessioni
socket_heartbeat.listen(1)
print("Servers TCP in attesa di connessioni...")

# Accetta una connessione
recive_command, address1 = socket_command.accept()  # Bloccante
print("Connessione Command")
recive_heartbeat, address2 = socket_heartbeat.accept()  # Bloccante
print("Connessione Heartbeat")

thread_heartbeat = threading.Thread(target=heartbeat_recive, args=(recive_heartbeat,))
thread_heartbeat.start()

while True:
    # Riceve dal client
    data = recive_command.recv(4096)  # Bloccante

    match data.decode():
        case "Avanti":
            # Alphabot.forward()
            print("Avanti")
        case "Stop Avanti":
            # Alphabot.forward()
            print("Fermo avanti")
        case "Indietro":
            # Alphabot.forward()
            print("Indietro")
        case "Stop Indietro":
            # Alphabot.forward()
            print("Fermo indietro")
        case "Sinistra":
            # Alphabot.forward()
            print("Sinistra")
        case "Stop Sinistra":
            # Alphabot.forward()
            print("Fermo Sinistra")
        case "Destra":
            # Alphabot.forward()
            print("Destra")
        case "Stop Destra":
            # Alphabot.forward()
            print("Fermo Destra")
        case "esc":
            break

socket_heartbeat.close()  # Chiudi il socket dopo l'uscita dal ciclo
socket_command.close()
# Alphabot.stop()
