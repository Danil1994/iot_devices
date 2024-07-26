from aiohttp import web
from aiohttp_swagger import *


async def ping(request):
    """
    ---
    description: This end-point allow to test that service is up.
    tags:
    - Health check
    produces:
    - text/plain
    responses:
        "200":
            description: successful operation. Return "pong" text
        "405":
            description: invalid HTTP Method
    """
    return web.Response(text="pong")


app = web.Application()
app.router.add_route('GET', "/ping", ping)

setup_swagger(app)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port=8090)
