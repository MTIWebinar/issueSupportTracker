# -*- coding:utf-8 -*-

import socket
import sys
import json


HOST, PORT = '127.0.0.1', 4001


# data = ' '.join(sys.argv[1:]).split() # первый агрумент - это путь
json_encoded = json.dumps(['test json', {'tag1': 'hello', 'tag2': 'word'}])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall(json_encoded.encode('utf-8'))

    received = sock.recv(1024).decode('utf-8')
finally:
    sock.close()

print(u'Sent: {:>14}'.format(json_encoded))
print(u'Received: {:>10}'.format(received))