import socket
import AlphaBot

istanza = AlphaBot()

# Crea un socket TCP
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa il socket a un indirizzo e una porta
server_address = ("localhost", 12345)
tcp_server_socket.bind(server_address)

# il server ascolta le connessioni in entrata
tcp_server_socket.listen(1)  # Dimensione coda connessioni
print("Server TCP in attesa di connessioni...")

# Accetta una connessione
conn, address = tcp_server_socket.accept()  # Bloccante
print(f"Connessione stabilita con {address}")

# Riceve dal client
data = conn.recv(4096)  # Bloccante
print(f"Messaggio ricevuto: {data.decode()}")

# Invia una risposta al client
conn.sendall(b"Messaggio ricevuto!")
conn.close()
