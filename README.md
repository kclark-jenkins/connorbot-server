# connorbot-server
This is the RPC Server for ConnorBot.  This RPC server serves as the bridge between the NodeJS webapp and the physical hardware controlled via python.

# Current status
This code is not functional as of 10/22/2017 except as an RPC server showing the commands being sent from client to server and back.  The code that controls the motors is working but being cleaned up as it's current level of working is best described as "prototype".

Check back frequently to see if the entire project has been published.  Once stable all code will be in this project.

# Configuration
connorbot-server is configured in connorbot.ini

The following is the default configuration

```
[rpc]
port = 4242
listenAddress = 0.0.0.0
protocol = tcp

[direction]
FORWARD  = 1
BACKWARD = 2
LEFT     = 3
RIGHT    = 4
RIGHT90  = 5
LEFT90   = 6
ABOUT    = 7
ROTATION = 8
```

# Installation

## Required Software
* Python
* Pip
* ZeroMQ

## Server side

```
pip install zerorpc
pip install configparser
cd ~
git clone https://github.com/kclark-jenkins/connorbot-server.git
```

## Client side

* Windows
  * [Install ZeroMQ for Windows](http://zeromq.org/docs:windows-installations)
* Linux
  * [Install ZeroMQ for Linux](http://zeromq.org/intro:get-the-software)
* OS X
  * [Install ZeroMQ for OS X](http://zeromq.org/docs:source-git#toc2)


# Testing

## Start on the server

```
cd ~
cd connorbot-server
python ./ConnorBot.py
```

## Expected output with default config

```
ConnorBotRPC online and listening on tcp://0.0.0.0:4242
```

## Send message

Open up a terminal or cmd.exe depending on your client operating system

```
zerorpc tcp://hostname:4242 move 1 1 --json
```

## Expected output (as of 10/22/2017)

```
zerorpc tcp://127.0.0.1:4242 move 1 1 --json
connecting to "tcp://127.0.0.1:4242"
'I'
'm'
'p'
'l'
'e'
'm'
'e'
'n'
't'
' '
'm'
'o'
't'
'o'
'r'
' '
'c'
'o'
'd'
'e'
' '
'f'
'r'
'o'
'm'
' '
'p'
'i'
' '
'p'
'r'
'o'
't'
'o'
't'
'y'
'p'
'e'
```