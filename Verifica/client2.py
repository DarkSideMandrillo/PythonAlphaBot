import time
import datetime
import socket
import random


def main():
    
    stazioneID = 1

    socket_tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_tcp.connect(("127.0.0.1",12345))
    
    while True:
      valore = random.randint(1,10)
      data = datetime.datetime.now()
      messaggio = str(stazioneID) + "|" + str(data) + "|" + str(valore)
      print(messaggio)
      socket_tcp.sendall(messaggio.encode())

      response_recive = socket_tcp.recv(4092)
      if response_recive.decode() == "3":
         print("avvenuto invio")
         print("ACCENDI SIRENA")
      else:
         print("avvenuto invio")
         
      time.sleep(15)

if __name__ == "__main__":
    main()  # Esegui la funzione principale



"id|data e ora|livello"
"1|2024-11-16 16:41:26.985785|3.6"