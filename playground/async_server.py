import asyncio

rsp_dict = {"palm.cpu": [ (1150864247, 0.5), (1150864248, 0.5) ] }

def create_message(key):
    list_values = rsp_dict[key]
    msg = "ok\n"
    for item in list_values:
        msg += "{} {} {}\n".format(key, str(item[-1]), str(item[0]))
    msg += "\n"
    print(msg)
    return msg
    # return "ok\n\n"

async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    command = message.rstrip().split(" ")
    print(command)
    addr = writer.get_extra_info("peername")
    print("recived {} from {}\n".format(message, addr))
    if command[0] == "get":
        response = create_message(command[-1])
    else:
        response = "ok\n\n" 
    writer.write(response.encode("utf8"))
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001, loop=loop)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()