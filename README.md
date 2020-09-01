# OPC UA Server and Client (Python)
Setup of a OPC UA Server on Raspberry Pi using Python

## Installation

Run these commands on the Raspberry Pi

$ sudo apt-get update

$ sudo apt-get install libxml2-dev libffi-dev

$ sudo pip3 install cryptography

$ sudo pip3 install freeopcua

## RUN
$python3 server.py

or

$python3 client.py


## Tutorial Videos for setting up OPCUA Server
https://www.youtube.com/watch?v=mEbPHflLNyc


# OPC UA Client (node js)

## Tutorial and setup
https://github.com/node-opcua/node-opcua/blob/v0.4.1/documentation/creating_a_client.md

# Protobuf

## How to get up and running with Protobuf
http://osdevlab.blogspot.com/2016/03/how-to-install-google-protocol-buffers.html

## Compile Protobuf Protocol Message
``` 
$ protoc addressbook.proto --python_out="."
```

