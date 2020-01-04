# **RedNet**

### A UDP DDos botnet that you can flood udp packets.
> Is under development

## Usage

### Server: Accepts connections and redirects commands to bots
- ``` python3 server.py ``` **(python3)**

### Client: Connects to the server, waits for commands, and executes them.
- ``` python client.py ``` **(It depends on the modules) (python2)**

### root_cient: Connects to the server, and allows you to send commands to the bots.
- ``` python root_client.py ``` **(python2)**

## Commands
- ``` !bots ``` **Returns the number of bots actives.**
- ``` !udpflood.start IP:PORT ``` **Starts UDP Flood DDos Attack, with 255 threads**
- ``` !udpflood.stop ``` **Stop the attack**

## Modify it
- ``` user_required and pass_required on server.py ``` **(It is the username and password that the attacker will use to control the bots.)**
