import asyncio
import time
from random import randint


async def producer(identifier, queue):
    sleep_time = randint(0, 4)
    message = {'id': identifier, 'sleep_time': sleep_time}
    await queue.put(message)
    print(f'Producer {identifier} added task to queue with message {message}.')


async def my_consumer(name, queue):
    while queue.qsize():
        message = await queue.get()

        print(f'{name} captured message {message}.')
        await asyncio.sleep(message['sleep_time'])
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    producers = [loop.create_task(producer(n, queue)) for n in range(30)]
    consumer1 = loop.create_task(my_consumer('consumer1', queue))
    consumer2 = loop.create_task(my_consumer('consumer2', queue))
    consumer3 = loop.create_task(my_consumer('consumer3', queue))
    await asyncio.gather(*producers)
    await queue.join()  # Implicitly awaits consumers, too
    consumer1.cancel()
    consumer2.cancel()
    consumer3.cancel()

if __name__ == '__main__':
    start = time.perf_counter()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    elapsed = time.perf_counter() - start
    print(f'Program completed in {elapsed:0.5f} seconds.')
