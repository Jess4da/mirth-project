import socket
import json
import time as t
from .config import config


class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = config['SERVER']['ip']
        self.port = int(config['SERVER']['port'])
        self.addr = (self.server, self.port)
        self.name = name
        self.connect()

    def connect(self):
        self.__status = 1
        try:
            self.client.connect(self.addr)

            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)

    def send(self, data):
        try:
            self.client.send(json.dumps(data).encode())
            d = ""
            while 1:
                last = self.client.recv(1024).decode()
                d += last
                try:
                    if d.count(".") == 1:
                        break
                except:
                    pass

            try:
                if d[-1] == ".":
                    d = d[:-1]
            except:
                pass
            keys = [key for key in data.keys()]
            return json.loads(d)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)

    def status(self):
        return self.__status

    def disconnect(self, msg):
        print("[EXCEPTION] Disconnected from server:", msg)
        self.__status = 0
        self.client.close()
