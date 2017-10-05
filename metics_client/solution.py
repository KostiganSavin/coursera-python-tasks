# import asyncio
import socket
import time

class Client:

    def __init__(self, addr, port, timeout=None):
        self.sock = socket.create_connection((addr, port), timeout=timeout)
    
    def put(self, key, value, timestamp=None):
        self.sock.settimeout(1)
        timestamp = timestamp or int(time.time())
        message = "put {0} {1} {2}".format(key, str(value), str(timestamp))
        self.sock.sendall(message.encode("utf8"))
        data = self.sock.recv(1024)
        print(data.decode())
        self.sock.close()    

    def get(self, key):
        pass


def _main():
    client = Client("127.0.0.1", 10001, timeout=15)
    client.put("palm.cpu", 0.5, timestamp=1150864247)

if __name__ == "__main__":
    _main()