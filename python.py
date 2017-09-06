import sys
import socket

argumento1 = sys.argv[1]

argumento2 = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = argumento1
port  = argumento2
port = int(port)


try:
    s.connect((ip, port))
    while True:
        mensagem = raw_input("")
        s.send(mensagem+"\n")


except Exception as erro:
    print erro
