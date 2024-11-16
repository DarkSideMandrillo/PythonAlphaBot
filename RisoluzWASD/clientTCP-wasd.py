import socket
from pynput import keyboard
import threading
import time

# Variabili di stato per controllare se un tasto è attualmente premuto
keys_pressed = {"w": False, "a": False, "s": False, "d": False, "q": False}

# Creo Socket Globale per velocizzare
# Crea due un socket COMANDI e HEARTBEAT
socket_comandi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_heartbeat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connetti il socket al COMANDI
socket_comandi.connect(("localhost", 12345))
# Connetti il socket al HEARTBEAT
socket_heartbeat.connect(("localhost", 12346))


# Funzione chiamata quando un tasto viene premuto
def on_press(key):
    try:
        if key.char in keys_pressed and not keys_pressed[key.char]:
            keys_pressed[key.char] = True  # Imposta il tasto come premuto
            comando = ""
            if key.char == "w":
                comando = b"Avanti"
            elif key.char == "a":
                comando = b"Sinistra"
            elif key.char == "s":
                comando = b"Indietro"
            elif key.char == "d":
                comando = b"Destra"
            socket_comandi.sendall(comando)

    except AttributeError:
        # Ignora tasti speciali come Shift, Ctrl, etc.
        pass


# Funzione chiamata quando un tasto viene rilasciato
def on_release(key):
    try:
        if key.char in keys_pressed and keys_pressed[key.char]:
            keys_pressed[key.char] = False  # Imposta il tasto come non premuto
            comando = ""
            if key.char == "w":
                comando = b"Stop Avanti"
            elif key.char == "a":
                comando = b"Stop Sinistra"
            elif key.char == "s":
                comando = b"Stop Indietro"
            elif key.char == "d":
                comando = b"Stop Destra"
            elif key.char == "q":
                comando = b"esc"
                return False

            socket_comandi.sendall(comando)
    except AttributeError:
        pass


def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Attivazione tasti")
        listener.join()


def heartbeat_send():
    while True:
        socket_heartbeat.sendall(b"connesso")
        time.sleep(1.5)


def main():
    # Creazione del thread
    thread_heartbeat = threading.Thread(target=heartbeat_send)
    thread_heartbeat.start()

    # Parte l'ascolto dei tasti
    start_listener()

    socket_comandi.close()
    socket_heartbeat.close()


if __name__ == "__main__":
    main()
