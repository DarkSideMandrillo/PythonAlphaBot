import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ServerAlphaBot')))

#import RPi.GPIO as GPIO
from ServerAlphaBot.AlphaBot import Alphabot
import socket

# Inizializzo il robot
robot = Alphabot()

# Crea un socket TCP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa il socket a un indirizzo e una porta
server_address = ("localhost", 12345)
tcp_server_socket.bind(server_address)

# il server ascolta le connessioni in entrata
tcp_server_socket.listen(1)  # Dimensione coda connessioni

# Accetta una connessione
conn, address = tcp_server_socket.accept()

# Riceve dal client
data = conn.recv(4096)
print(f"Messaggio ricevuto: {data.decode()}")


# Invia una risposta al client
conn.sendall(b"Messaggio ricevuto!")
conn.close()
