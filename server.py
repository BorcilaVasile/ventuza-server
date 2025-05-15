import socket
import os

port = int(os.getenv("PORT", 4242))
host = '0.0.0.0'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f"Ascult pe portul {port}...")
    conexiune, adresa = s.accept()
    with conexiune:
        print('Conectat de', adresa)
        while True:
            comanda = input("Introduceți comanda: ")
            if comanda.lower() == 'exit':
                break
            conexiune.sendall(comanda.encode())
            date = conexiune.recv(1024)
            print("Rezultat:", date.decode())