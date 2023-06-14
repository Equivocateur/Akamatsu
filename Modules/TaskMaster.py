import asyncio


class TaskMaster:

    def __init__(self, parent):
        self.parent = parent
        self.loop = None

    async def setuploop(self):
        self.loop = asyncio.get_event_loop()

    async def createtask(self, task, *args):
        print(f"A task for {task.__name__} has been started.")
        self.loop.create_task(task(*args))
