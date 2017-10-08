import asyncio


@asyncio.coroutine
def hello_world():
    while True:
        print("Hello World")
        yield from asyncio.sleep(1)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(hello_world())
except KeyboardInterrupt:
    pass
loop.close()