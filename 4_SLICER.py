import asyncio
from asyncio import sleep

loop = asyncio.get_event_loop()


class MySlicer:
    def __init__(self, internal_list):
        self.internal_list = internal_list

    async def _get(self, key):
        await sleep(0.1)
        return self.internal_list[key]

    async def __getitem__(self, key):
        if isinstance(key, slice):
            return MySlicer(self.internal_list[key])
        elif isinstance(key, int):
            return await self._get(key)
        raise TypeError('Incorrect key type')

    def __str__(self):
        return f'slicer {self.internal_list}'


async def slicer_fun():
    first_slicer = MySlicer(list(range(50)))
    print(f'first slicer: {first_slicer}')
    last_item_first_slicer = await first_slicer[-1]
    print(f'last_item_first_slicer: {last_item_first_slicer}')

    second_slicer = await first_slicer[10:]
    print(f'second slicer: {second_slicer}')
    first_item_second_slicer = await second_slicer[0]
    print(f'first_item_second_slicer: {first_item_second_slicer}')

loop.create_task(slicer_fun())

tasks = asyncio.Task.all_tasks()
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
