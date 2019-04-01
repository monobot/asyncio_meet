import asyncio
import time

loop = asyncio.get_event_loop()

# Yoou can start the loop, so it runs a task and then finishes
start = time.perf_counter()
loop.run_until_complete(asyncio.sleep(1))
timeit = time.perf_counter() - start

print(timeit)

# You can create some tasks and finish when all of then are done
start = time.perf_counter()
loop.create_task(asyncio.sleep(1))

tasks = asyncio.Task.all_tasks()
loop.run_until_complete(asyncio.gather(*tasks))
timeit = time.perf_counter() - start

print(timeit)

# If you close the event loop then you can not use it again
loop.close()


import pdb; pdb.set_trace()
loop.create_task(asyncio.sleep(1))
