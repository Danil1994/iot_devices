from aiohttp import web
from aiohttp_swagger import *
from api.handlers import all_device, create_device, update_device, get_device, delete_device

from init_db import initialize_database

initialize_database()

app = web.Application()

app.add_routes([
    web.get('/devices', all_device),
    web.post('/devices', create_device),
    web.get('/devices/{id}', get_device),
    web.put('/devices/{id}', update_device),
    web.delete('/devices/{id}', delete_device),
])

setup_swagger(app, swagger_url="/api/v1/doc", ui_version=2)

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port=8080)
