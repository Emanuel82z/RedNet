# **RedNet**

### A simple DDos botnet
> Is under development

## Usage

### Server: Accepts connections and redirects commands to bots
- ``` python3 server.py ``` **(python3)**

### Client: Connects to the server, waits for commands, and executes them.
- ``` python client.py ``` **(It depends on the modules) (python2)**

### root_cient: Connects to the server, and allows you to send commands to the bots.
- ``` python root_client.py --host IP --port PORT ``` **(python2)**

## Commands
- ``` !bots ``` **Returns the number of bots actives.**
- ``` !udpflood.start IP:PORT ``` **Starts UDP Flood DDos Attack**
- ``` !slowloris.start IP:PORT ``` **Starts SlowLoris Attack**

## Variables to modify
- ``` user_required and pass_required on server.py ``` **(It is the username and password that the attacker will use to control the bots.)**
- ``` user and password on root_client.py ``` **(Is the username and password that will be sent when connecting)**
- ``` IP and PORT ``` **(On server.py and client.py)**

## Server based on: 
### https://gist.github.com/schedutron/cd925247bfc4f8ae7930bbd99984a441#file-chat_serv-py
