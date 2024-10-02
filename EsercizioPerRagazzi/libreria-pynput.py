from pynput import keyboard


# Funzione chiamata quando un tasto viene premuto
def on_press(key):
    # try:
    if key.char == "w":
        print("press w")


# except AttributeError:
#     # Ignora tasti speciali come Shift, Ctrl, etc.
#     pass


# Funzione chiamata quando un tasto viene rilasciato
def on_release(key):
    # try:
    if key.char == "w":
        print("release w")


# except AttributeError:
#     pass


def start_listener():
    # Listener per intercettare gli eventi della tastiera
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


start_listener()
