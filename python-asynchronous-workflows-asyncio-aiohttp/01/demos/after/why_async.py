import asyncio
import time

async def call_api():
    print("start api call")
    # await asyncio.sleep(1)
    time.sleep(1)
    print("end api call")


async def main():
    start_time = time.perf_counter()
    
    task = asyncio.create_task(call_api()) # start
    await call_api() # start + finish

    await task # finish

    end_time = time.perf_counter()
    print(f'Duration: {round(end_time-start_time,2)}')


asyncio.run(main())
