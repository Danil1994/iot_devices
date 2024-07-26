import json
from aiohttp import web
from db.config_db import db
from db.models import Device


async def all_device(request):
    """
    ---
    description: Retrieve all devices.
    tags:
    - Devices
    produces:
    - application/json
    responses:
        "200":
            description: A list of devices
        "400":
            description: Bad request
    """
    db.connect()
    devices = Device.select()
    devices_list = []

    for device in devices:
        devices_list.append({
            "id": device.id,
            "user_id": device.user_id.id,
            "location_id": device.location_id.id,
            "name": device.name,
            "type": device.type,
            "login": device.login,
            "password": device.password
        })
    db.close()

    return web.Response(text=json.dumps(devices_list), content_type='application/json')


async def create_device(request):
    """
    ---
    description: Create a new device.
    tags:
    - Devices
    consumes:
    - application/json
    parameters:
    - in: body
      name: device
      description: The device to create
      schema:
        type: object
        required:
          - user_id
          - location_id
          - name
          - type
          - login
          - password
        properties:
          user_id:
            type: integer
          location_id:
            type: integer
          name:
            type: string
          type:
            type: string
          login:
            type: string
          password:
            type: string
    responses:
        "201":
            description: Device created successfully
        "400":
            description: Bad request
    """
    db.connect()
    try:
        data = await request.json()
        device = Device.create(
            user_id=data['user_id'],
            location_id=data['location_id'],
            name=data['name'],
            type=data['type'],
            login=data['login'],
            password=data['password']
        )
        db.close()
        return web.json_response({
            "id": device.id,
            "user_id": device.user_id.id,
            "location_id": device.location_id.id,
            "name": device.name,
            "type": device.type,
            "login": device.login,
            "password": device.password
        }, status=201)
    except Exception as e:
        db.close()
        return web.json_response({"error": str(e)}, status=400)


async def update_device(request):
    """
    ---
    description: Update an existing device.
    tags:
    - Devices
    consumes:
    - application/json
    parameters:
    - in: path
      name: id
      required: true
      type: integer
      description: The device ID
    - in: body
      name: device
      description: The device data to update
      schema:
        type: object
        properties:
          user_id:
            type: integer
          location_id:
            type: integer
          name:
            type: string
          type:
            type: string
          login:
            type: string
          password:
            type: string
    responses:
        "200":
            description: Device updated successfully
        "400":
            description: Bad request
    """
    db.connect()
    try:
        device_id = request.match_info.get('id')
        data = await request.json()
        device = Device.get(Device.id == device_id)

        device.user_id = data.get('user_id', device.user_id)
        device.location_id = data.get('location_id', device.location_id)
        device.name = data.get('name', device.name)
        device.type = data.get('type', device.type)
        device.login = data.get('login', device.login)
        device.password = data.get('password', device.password)

        device.save()
        db.close()

        return web.json_response({
            "id": device.id,
            "user_id": device.user_id.id,
            "location_id": device.location_id.id,
            "name": device.name,
            "type": device.type,
            "login": device.login,
            "password": device.password
        }, status=200)
    except Exception as e:
        db.close()
        return web.json_response({"error": str(e)}, status=400)


async def get_device(request):
    """
    ---
    description: Get a device by ID.
    tags:
    - Devices
    produces:
    - application/json
    parameters:
    - in: path
      name: id
      required: true
      type: integer
      description: The device ID
    responses:
        "200":
            description: Device details in JSON format
        "400":
            description: Bad request
    """
    db.connect()
    try:
        device_id = request.match_info.get('id')
        device = Device.get(Device.id == device_id)

        device_data = {
            "id": device.id,
            "user_id": device.user_id.id,
            "location_id": device.location_id.id,
            "name": device.name,
            "type": device.type,
            "login": device.login,
            "password": device.password
        }

        db.close()
        return web.json_response(device_data, status=200)

    except Device.DoesNotExist:
        db.close()
        return web.json_response({"error": "Device not found"}, status=404)

    except Exception as e:
        db.close()
        return web.json_response({"error": str(e)}, status=500)


async def delete_device(request):
    """
    ---
    description: Delete a device by ID.
    tags:
    - Devices
    produces:
    - text/plain
    parameters:
    - in: path
      name: id
      required: true
      type: integer
      description: The device ID
    responses:
        "200":
            description: Device deleted successfully
        "400":
            description: Bad request
    """
    db.connect()
    device_id = request.match_info.get('id')
    device = Device.get(Device.id == device_id)
    device.delete_instance()
    db.close()

    return web.Response(status=200, text='Device deleted successfully')
