from aiohttp import ClientSession
import asyncio

from custom_event_loop import TimingEventLoopPolicy

API_URLS = [
    "http://localhost:8080/names/1",
    "http://localhost:8080/names/2",
] * 1000

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def fetch_all():
    async with ClientSession() as session:
        tasks = [fetch(session, url) for url in API_URLS]
        results = await asyncio.gather(*tasks)

asyncio.set_event_loop_policy(TimingEventLoopPolicy())
asyncio.run(fetch_all())