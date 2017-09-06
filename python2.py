import socket
import sys

argumento1 = sys.argv[1]

argumento2 = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '0.0.0.0'
port = argumento2
port = int(port)

if argumento1 == '-lvp':
    try:
        s.bind((ip, port))
        s.listen(5)
        print ("Listening on [any]",port)
        s.accept()
        while True:
            data = s.recv(1024)
            print data

    except Exception as erro:
        print erro

