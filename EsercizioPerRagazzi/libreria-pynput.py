from pynput import keyboard
import time

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


def lib_time():
    # Ottieni l'ora corrente
    current_time = time.time()
    print("Epoch Time:", current_time)

    # Formatta il tempo in modo leggibile
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("Formatted Time:", formatted_time)

    # Cronometrare il tempo di esecuzione
    start = time.perf_counter()
    time.sleep(1)  # Simula un ritardo di 1 secondo
    end = time.perf_counter()
    print(f"Elapsed Time: {end - start:.4f} seconds")

lib_time()
time.sleep(5)
start_listener()
