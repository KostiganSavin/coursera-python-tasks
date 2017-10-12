import asyncio

metrics = {}

def run_server(host, port):
    pass


def _put(payload):
    global metrics
    # print("PUT: ", payload)
    key, value, timestamp = payload.split(" ")
    
    if not key in metrics:
        metrics[key] = []
        metrics[key].append((int(timestamp), float(value)))
    else:
        last_element = metrics[key].pop()
        # print(last_element)
        if last_element[0] == int(timestamp):
            metrics[key].append((int(timestamp), float(value)))
        else:
            metrics[key].append(last_element)
            metrics[key].append((int(timestamp), float(value)))
    # print(metrics)
    return "ok\n\n"


def _get(key):
    global metrics
    print("GET: ", key)
    resp = "ok\n"
    if key not in metrics and key !="*":
        return resp + "\n"

    if key == "*":
        print(metrics)
        for item in metrics:
            for values in metrics[item]:
                resp += "{0} {1} {2}\n".format(item, values[1], values[0])
    else:
        print(metrics[key])
        for values in metrics[key]:
            resp += "{0} {1} {2}\n".format(key, values[1], values[0])
    
    return resp + "\n"


def process_data(data):
    command, payload = data.split(" ", 1)
    
    if not command in commands:
        return "error\nwrong command\n\n"
    
    payload = payload.strip()
    
    return commands[command](payload)


commands = {"put": _put,
            "get": _get,
            }


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info("peername")
        print("Connection from {}".format(peername))
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())


loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8888
)

server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()