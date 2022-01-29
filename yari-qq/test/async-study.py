from datetime import datetime
from time import sleep
import asyncio

async def show():
    print("helloworld")
    await asyncio.sleep(1)
    return 'hello'
show()