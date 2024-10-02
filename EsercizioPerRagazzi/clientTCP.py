import socket

# TCP (Trasmission Control Protocol)
# Crea un socket TCP
tcp_client_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # Address Family - Internet

# Connetti il socket al server
server_address = ("localhost", 12345)
tcp_client_socket.connect(server_address)

# Messaggio da inviare
message = b"Ciao, server TCP!"  # trasforma la stringa da Unicode a formato byte

# Invia il messaggio
tcp_client_socket.sendall(message)  # Invia tutti i dati

# Ricevi risposta dal server
data = tcp_client_socket.recv(4092)
print(f"Risposta del server: {data.decode()}")

tcp_client_socket.close()
