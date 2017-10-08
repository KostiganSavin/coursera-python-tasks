import socket
import time

class Client:

    def __init__(self, addr, port, timeout=None):
        self.addr = addr
        self.port = port
        self.timeout = timeout

    def put(self, key, value, timestamp=None):
        with socket.create_connection((self.addr, self.port), self.timeout) as conn: 
        # with self._connect() as conn: 
            # conn.settimeout(2)
            timestamp = timestamp or int(time.time())
            message = "put {0} {1} {2}\n".format(key, str(value), str(timestamp))
            try:
                conn.sendall(message.encode("utf8"))
                data = conn.recv(1024)
                # print(data.decode("utf8"))
                if data.decode("utf8") != "ok\n\n":
                    raise ClientError
            except socket.timeout:
                raise ClientError

    def get(self, key):
        with socket.create_connection((self.addr, self.port), self.timeout) as conn:
            message = "get {}\n".format(key)
            print(message)
            try:
                conn.sendall(message.encode("utf8"))
                data = conn.recv(1024)
                if data.decode("utf8").endswith("\n\n"):
                    if data.decode("utf8").startswith("ok"):
                        result = {}
                        recived_data_list = data.decode("utf8")[3:-2].split("\n")
                        if not len(recived_data_list) == 1:
                            for item in recived_data_list:
                                key, value, timestamp = item.split(" ")
                                result[key] = result.get(key, []) + [(int(timestamp), float(value))]
                        return result
                    elif data.decode("utf8").startswith("error"):
                        raise ClientError

            except socket.timeout:
                raise ClientError                


class ClientError(Exception):
    pass

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

if __name__ == "__main__":
    _main()