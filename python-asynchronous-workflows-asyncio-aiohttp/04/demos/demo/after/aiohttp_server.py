import asyncio
from aiohttp import web

names_db = {
    1: "Sophia",
    2: "Michael"
}

async def get_names(request):
    return web.json_response(names_db)

async def get_name_by_id(request):
    name_id = request.match_info.get('id')
    response = {
        "id": name_id,
        "name": names_db[int(name_id)]
    }
    return web.json_response(response)


async def add_name(request):
    data = await request.json()
    new_id = len(names_db) + 1
    names_db[new_id] = data.get("name")
    return web.json_response({"id": new_id, "name": names_db[new_id]})

async def sse_handler(request):
    r = web.StreamResponse()
    r.headers['Content-Type'] = 'text/event-stream'
    r.headers['Cache-Control'] = 'no-cache'
    r.headers['Connection'] = 'keep-alive'
    await r.prepare(request)
    counter = 0
    while counter < 3:
        counter += 1
        data = "Temperature: 70 \n"
        await r.write(data.encode('utf-8'))
        await asyncio.sleep(1)
    await r.write_eof()


app = web.Application()

app.router.add_get('/names', get_names)
app.router.add_get('/names/{id}', get_name_by_id)
app.router.add_post('/names', add_name)

app.router.add_get("/events", sse_handler)

# web.run_app(app)
