#!/usr/bin/python
from urllib import urlopen
from socket import socket, SOCK_DGRAM, AF_INET
s = socket(AF_INET, SOCK_DGRAM)
s.connect(('google.com', 0))
print('Local  IP: '+s.getsockname()[0])
print('Public IP: '+urlopen('http://ipv4bot.whatismyipaddress.com/').read().replace('\n', ''))
