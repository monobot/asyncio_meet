import asyncio
import concurrent.futures


def power_func(x, y):
    return x ** y


async def my_base_coroutine(x, y):
    executor = concurrent.futures.ProcessPoolExecutor()
    results = await loop.run_in_executor(executor, power_func, x, y)
    print(f'FINISHED TASK {x}^{y}={results}')
    return results

loop = asyncio.get_event_loop()

loop.create_task(my_base_coroutine(9, 767))
loop.create_task(my_base_coroutine(2, 3))
loop.create_task(my_base_coroutine(5, 57))

tasks = asyncio.Task.all_tasks()
loop.run_until_complete(asyncio.gather(*tasks))
