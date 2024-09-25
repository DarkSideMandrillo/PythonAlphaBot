import sys
import os

def add_paths():
    """Aggiungi i percorsi delle cartelle Client e ServerAlphaBot."""
    sys.path.append(os.path.abspath('Client'))
    sys.path.append(os.path.abspath('ServerAlphaBot'))

def main():
    """Funzione principale per eseguire il programma."""
    import wasd
    wasd.start_listener()


if __name__ == "__main__":
    add_paths()  # Aggiungi i percorsi prima di eseguire il main
    main()  # Esegui la funzione principale
