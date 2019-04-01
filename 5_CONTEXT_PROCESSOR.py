import asyncio
from asyncio import sleep

loop = asyncio.get_event_loop()


class Connection:
    connected = False

    async def connect(self):
        await sleep(0.1)
        self.connected = True

    async def disconnect(self):
        await sleep(0.1)
        self.connected = False


class MyContextProcessor:
    def __init__(self):
        self.connection = Connection()

    def is_connected(self):
        return self.connection.connected

    async def __aenter__(self):
        await self.connection.connect()
        return self

    async def __aexit__(self, *args):
        await self.connection.disconnect()
        self.connection = None


async def check_context_processor():
    async with MyContextProcessor() as context_processor:
        print(f'inside the with statement i am connected: {context_processor.is_connected()}')

loop.run_until_complete(check_context_processor())
loop.close()
