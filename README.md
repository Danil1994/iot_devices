# IoT Device Management App

This is a simple application for managing IoT devices using Python, PostgreSQL, peewee ORM, and aiohttp for creating an
asynchronous API.

## Requirements

- Python 3.7+
- PostgreSQL

## Install

1. Clone repo:

* Clone with SSH `git clone git@github.com:Danil1994/iot_devices.git`
* Clone with HTTPS `git clone https://github.com/Danil1994/iot_devices.git`

1. Go to your project folder: `path/to/the/folder`
2. Create and activate a virtual environment
3. Load your .env file to the project like .env.example
4. Install requirements.txt run: `pip install -r requirements.txt`
5. Create database PostgreSQL and configure connection parameters

## Run

1. Run server: `python app.py`
2. Run `python create_fake_data.py` to create fake data
3. Go to link `http://127.0.0.1:8080/api/v1/doc#/Devices` in your browser

## Using

Application use basic CRUD operations.

* GET `/devices` retrieve all devices.
* POST `/devices` create a new device.
* GET `/devices/{id}` get a device by ID.
* PUT `/devices/{id}` update an existing device.
* DELETE `/devices/{id}` delete a device by ID.

# Database Models
The application uses the following database models:

User (api_user table):

    name: CharField
    email: CharField (unique)
    password: CharField

Device (device table):

    name: CharField
    type: CharField
    login: CharField
    password: CharField
    location_id: ForeignKeyField to Location
    api_user_id: ForeignKeyField to User

Location (location table):

    name: CharField
