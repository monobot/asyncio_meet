import asyncio
import concurrent.futures
import time


def complex_calculation(x):
    time.sleep(x)
    return x


async def my_base_coroutine(x):
    print(f'STARTING TASK {x}')
    executor = concurrent.futures.ProcessPoolExecutor()
    await loop.run_in_executor(executor, complex_calculation, x)
    print(f'FINISHED TASK {x}')

loop = asyncio.get_event_loop()

loop.create_task(my_base_coroutine(5))
loop.create_task(my_base_coroutine(3))
loop.create_task(my_base_coroutine(0.5))

print('Starting the whole process')
start = time.perf_counter()

tasks = asyncio.Task.all_tasks()
loop.run_until_complete(asyncio.gather(*tasks))

timeit = time.perf_counter() - start
print(f'Finished in {timeit} seconds.')
