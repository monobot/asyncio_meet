import asyncio
import time
from asyncio import sleep

loop = asyncio.get_event_loop()


async def my_first_coroutine(seconds):
    print(f'...starting the query {seconds}')
    await sleep(seconds)
    print(f'...finished the query {seconds}')

loop.create_task(my_first_coroutine(5))
loop.create_task(my_first_coroutine(3))
loop.create_task(my_first_coroutine(0.5))

print('Starting the whole process')
start = time.perf_counter()

tasks = asyncio.Task.all_tasks()
loop.run_until_complete(asyncio.gather(*tasks))

timeit = time.perf_counter() - start
print(f'Finished in {timeit} seconds.')
