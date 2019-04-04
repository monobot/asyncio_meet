import asyncio
from asyncio import sleep

loop = asyncio.get_event_loop()


class MyIterator:
    def __init__(self):
        self.wait = 0

    async def __aiter__(self):
        return self

    async def __anext__(self):
        if self.wait == 3:
            raise StopAsyncIteration
        self.wait += 1
        await sleep(self.wait)
        return self.wait


async def iterate_over():
    iterator = MyIterator()
    async for result in iterator:
        print(result)

loop.run_until_complete(iterate_over())
loop.close()
