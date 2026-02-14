from aiohttp import web

async def get_names(request):
    return web.Response(text='hi all')

app = web.Application()

app.router.add_get('/names', get_names)

web.run_app(app)