import datetime
import threading
import socket
import sqlite3

class connRaspberry(threading.Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.connectionDB = sqlite3.connect("fiumi.db",check_same_thread=False)
        self.cur = self.connectionDB.cursor()
    def run(self):
        try:
          while True:
            # Si mette in ascolto
            msg_rec = self.conn.recv(4092)
            msg_rec = msg_rec.decode()
            msg_rec = msg_rec.split("|")
            print(msg_rec)
            id_station = msg_rec[0]
            date = msg_rec[1]
            river_level = float(msg_rec[2])



            # Estrae il valore del fiume in questione

            self.cur.execute(f'''SELECT * FROM livelli WHERE id_stazione= {id_station}''')
            self.connectionDB.commit()
            river_station = self.cur.fetchall()
            river_guard_level = float(river_station[0][3])

            
            
            # Stampa il log
            print(f"Messaggio ricevuto dal fiume {river_station[0][1]} - località {river_station[0][2]} \nOre {date} \nLivello fiume {river_level}")

            # Controlla il livello
            control_allert = river_level*100/river_guard_level
            print(f"% problema {control_allert}")


            if control_allert < 30:
              return_message = 1

            elif control_allert < 70:
              return_message = 2
              print(f"pericolo imminente località {river_station[0][2]}")

            else:
              return_message = 3
              print(f"!!!pericolo!!! località {river_station[0][2]}")


          # Invia il messaggio con il segnale di allerta

            self.conn.sendall(str(return_message).encode())

        except:
           self.conn.close()
           self.connectionDB.close()

def main():

    socket_tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tcp.bind(("127.0.0.1",12345))
    print(datetime.datetime.now())
    socket_tcp.listen()
    while True:
      conn, addr = socket_tcp.accept()
      thread = connRaspberry(conn)
      thread.start()


if __name__ == "__main__":
    main()  # Esegui la funzione principale



"id|data e ora|livello"
"1|2024-11-16 16:41:26.985785|3.6"