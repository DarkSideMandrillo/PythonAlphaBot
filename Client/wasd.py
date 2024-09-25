from pynput import keyboard

# Variabili di stato per controllare se un tasto è attualmente premuto
keys_pressed = {
    'w': False,
    'a': False,
    's': False,
    'd': False,
    'q': False
}

# Funzione chiamata quando un tasto viene premuto
def on_press(key):
    try:
        if key.char in keys_pressed and not keys_pressed[key.char]:
            keys_pressed[key.char] = True  # Imposta il tasto come premuto

            if key.char == 'w':
                print("Avanti")
            elif key.char == 'a':
                print("Sinistra")
            elif key.char == 's':
                print("Indietro")
            elif key.char == 'd':
                print("Destra")

    except AttributeError:
        # Ignora tasti speciali come Shift, Ctrl, etc.
        pass

# Funzione chiamata quando un tasto viene rilasciato
def on_release(key):
    try:
        if key.char in keys_pressed and keys_pressed[key.char]:
            keys_pressed[key.char] = False  # Imposta il tasto come non premuto

            if key.char == 'w':
                print("Stop Avanti")
            elif key.char == 'a':
                print("Stop Sinistra")
            elif key.char == 's':
                print("Stop Indietro")
            elif key.char == 'd':
                print("Stop Destra")
            elif key.char == 'q':
                print("esc")
                return False

    except AttributeError:
        pass

def start_listener():
    # Listener per intercettare gli eventi della tastiera
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
