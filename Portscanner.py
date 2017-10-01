#encoding: utf -8
import socket


ip = raw_input("Ip ou Endereço :")

pergunta = raw_input("Deseja scanear apenas as portas mais usada ? S/N :")
pt = [21, 22 , 23, 24, 25, 80, 120 , 122 , 443, 1033]

ports = range(65300)


def contador(ip):
    numero = (int(raw_input("Quantas Portas deseja scanear ? :")))
    contadora = 0
    pu = []
    while contadora < numero:
        pu.append(int(raw_input("Informe ""a "+str(contadora + 1)+" PORTA :")))
        contadora += 1
    testar(ip, pu)

def testar(ip, ports):

    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05)
        resp = s.connect_ex((ip, port))

        if resp == 0:
            print str(port)+"==>> Porta Aberta <<==="
        else:
            print str(port)+"==>> Porta Fechada <<==="

def perguntas(ip, pt, ports, pergunta):
    if pergunta == 's':
        testar(ip, pt)

    if pergunta == 'n':
        var1 = raw_input ("Deseja scanear TODAS as portas de "+ip+" S/N ? :")
        if var1 == 's':
            testar(ip, ports)
        else:
            contador(ip)

perguntas(ip, pt ,ports, pergunta)