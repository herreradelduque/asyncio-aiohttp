import asyncio

async def call_api():
    print("calling")

async def main():
    await call_api()
    task = asyncio.create_task(call_api())
    await task

asyncio.run(main())
