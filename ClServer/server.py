#!/usr/bin/python
# -*- coding:utf-8 -*-

try:
    import SocketServer as socketserver
except ImportError:
    import socketserver

import json


HOST, PORT = '0.0.0.0', 4001

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).decode('utf-8')
        print(u'address: {}'.format(self.client_address[0]))
        js = self.json_decoder(self.data)[0]

        self.request.sendall(js.encode('utf-8'))

    def json_encoder(self, outJSON=None):
        pass

    def json_decoder(self, inJSON=None):
        data = json.loads(inJSON)
        print json.dumps(data, sort_keys=True, indent=4)
        return data

if __name__ == '__main__':

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()