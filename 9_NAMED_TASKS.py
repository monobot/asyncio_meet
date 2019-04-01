import asyncio
import logging
import time
from asyncio import sleep

loop = asyncio.get_event_loop()
loop.set_debug(True)

logging.basicConfig(level=logging.DEBUG)


async def coroutine(seconds):
    print(f'...starting the query {seconds}')
    await sleep(seconds)
    if seconds == 3:
        await coroutine(1)
    print(f'...finished the query {seconds}')

loop.create_task(coroutine(5), name='coroutine(5)')
loop.create_task(coroutine(3), name='coroutine(3)')
loop.create_task(coroutine(0.5), name='coroutine(0.5)')

print('Starting the whole process')
start = time.perf_counter()

tasks = asyncio.Task.all_tasks()

for t in tasks:
    print(t.get_name())

loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

timeit = time.perf_counter() - start
print(f'Finished in {timeit} seconds.')
