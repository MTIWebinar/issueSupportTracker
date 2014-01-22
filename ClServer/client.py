# -*- coding:utf-8 -*-

"""
Задачи:
1.
2.
3.

"""

import socket

import sys

HOST, PORT = '127.0.0.1', 4001

data = ' '.join(sys.argv[1:]) # первый агрумент - это путь

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall((data + '\n').encode('utf-8'))

    received = sock.recv(1024)
finally:
    sock.close()

print('Sent: {}'.format(data))
print('Received: {}'.format(received.decode('utf-8')))