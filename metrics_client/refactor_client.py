import socket
import time

class ClientError(Exception):
    pass


class Client:

    def __init__(self, addr, port, timeout=None):
        self.addr = addr
        self.port = port
        try: 
            self.connection = socket.create_connection((addr, port), timeout)
        except socket.error as err:
            raise ClientError ("error client connection", err)

    def _read(self):

        data = b""
        while not data.endswith(b"\n\n"):
            try:
                data += self.connection.recv(1024)
            except socket.error as err:
                raise ClientError("eroor while recive data", err)

        decoded_data = data.decode()

        status, payload = decoded_data.split("\n", 1)
        payload = payload.strip()

        if status == "error":
            raise ClientError(payload)

        return payload

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        message = "put {0} {1} {2}\n".format(key, str(value), str(timestamp))
        try:
            self.connection.sendall(message.encode("utf8"))
        except socket.error as err:
            raise ClientError("error sending data", err)

        self._read()


    def get(self, key):
        
        message = "get {}\n".format(key)
        try:
            self.connection.sendall(message.encode("utf8"))
        except socket.error as err:
            raise ClientError("error sending data", err)

        data = self._read()

        result = {}
        if data == "":
            return result
    
        for item in data.split("\n"):
            key, value, timestamp = item.split()
            result[key] = result.get(key, []) + [(int(timestamp), float(value))]
        
        return result

    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError("error close connnection", err)


def _main():
    client = Client("127.0.0.1", 10001, timeout=2)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)
    client.get("palm.cpu")

    client.close()

if __name__ == "__main__":
    _main()