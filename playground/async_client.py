import asyncio

async def tcp_echo_client(message, loop):

    try:
        while True:
            reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)
            print("send: {}".format(message))
            writer.write(message.encode())
            writer.close()
    except KeyboardInterrupt:
        pass

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(tcp_echo_client("Hello, World!", loop))
except KeyboardInterrupt:
    pass

loop.close()