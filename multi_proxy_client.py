import socket
from multiprocessing import Pool
import time

HOST = 'localhost'
PORT = 8001
BUFFER_SIZE = 1024

payload = 'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'

def connect(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    s.sendall(payload.encode())
    s.shutdown(socket.SHUT_WR)

    full_data = s.recv(BUFFER_SIZE)
    print(full_data)
    time.sleep(0.3)

def main():
    addr = [('127.0.0.1', 8002)]
    with Pool() as p:
        p.map(connect, addr * 10)

if __name__ == '__main__':
    main()
